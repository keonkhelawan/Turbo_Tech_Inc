from flask import Blueprint, render_template
from flask_login import current_user, login_required
skills_views = Blueprint('skills_views', __name__, template_folder='../templates')

from App.models import Skills, Course

@skills_views.route('/skills', methods=['GET'])
@login_required
def list_user_skills():
    user_skills = Skills.query.filter_by(userId=current_user.id).all()
    courses = Course.query.all()

    all_skills = []

    for eachSkill in user_skills:
        for eachCourse in courses:
            if(eachSkill.courseCode == eachCourse.courseCode):
                all_skills.append(eachCourse)

    return render_template('skills.html', skillsList=all_skills)