from flask import Blueprint, render_template
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
list_views = Blueprint('list_views', __name__, template_folder='../templates')

from App.models import Job
from App.models import Course
from App.controllers import course_code_splitting

'''@list_views.route('/list', methods=['GET'])
def get_user_page():
    list_of_jobs = Job.query.all()
    return render_template('list.html', jobData=list_of_jobs)'''


@list_views.route('/list', methods=['GET'])
@login_required
def collect_courses():
    course = Course.query.filter_by(userId=current_user.id).all()
    list_of_jobs = Job.query.all()

    courseCode_list = []
    jobs_to_render = []

    for eachCourse in course:
        courseCode_list.append(eachCourse.courseCode)

    for eachJob in list_of_jobs:
        result = course_code_splitting(eachJob.requirements, courseCode_list)

        if (result=="qualified"):
            jobs_to_render.append(eachJob)

    return render_template('list.html', jobData=jobs_to_render)        

