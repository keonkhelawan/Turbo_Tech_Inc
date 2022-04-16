from flask import Blueprint, render_template
from flask_login import current_user, login_required
list_views = Blueprint('list_views', __name__, template_folder='../templates')

from App.models import Job, Skills
from App.models import Course
from App.controllers import make_skill_list, list_jobs

#renders all jobs in the database when the "Jobs" button is pressed
@list_views.route('/jobs', methods=['GET'])
@login_required
def list_all_jobs():
    all_jobs = Job.query.all()
    '''all_courses = Course.query.all()'''
    return render_template('jobs.html', jobData=all_jobs)


# list all jobs that the current user is qualified for
@list_views.route('/list', methods=['GET'])
@login_required
def collect_courses():
    # adding user's skills to "courseSkills_list" and avoiding any duplicates
    courseSkills = Skills.query.filter_by(userId=current_user.id).all()

    skills = []
    for each in courseSkills:
        skills.append(each.courseSkills)

    courseSkills_list = make_skill_list(skills)  


    # comparing user's skills to skill requirements of each job within the database
    list_of_jobs = Job.query.all()
    jobs_to_render = []

    for eachJob in list_of_jobs:
        result = list_jobs(eachJob.competencies, courseSkills_list)

        if (result == "qualified"):
            jobs_to_render.append(eachJob)


    return render_template('list.html', jobData=jobs_to_render)        