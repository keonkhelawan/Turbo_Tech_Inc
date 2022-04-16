from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import  login_required, current_user
from App.models import Course, Skills
from App.database import db
from App.controllers import capital_letter

profile_views = Blueprint('profile_views', __name__, template_folder='../templates')

@profile_views.route('/profile', methods=['GET'])
@login_required
def get_user_page():
    skills = skills = Skills.query.filter_by(userId=current_user.id).all()
    return render_template('profile.html', courses=skills)


@profile_views.route('/profile', methods=['POST'])
@login_required
def update_user_page():
    data = request.form['text']

    check_course = capital_letter(data)
    if (check_course == "error"):
        flash('not a valid course code')
        return redirect(url_for('profile_views.get_user_page'))

    duplicate = Skills.query.filter_by(courseCode=check_course, userId=current_user.id).first()
    if duplicate:
        flash('course already in list')
        return redirect(url_for('profile_views.get_user_page')) 

    find_course = Course.query.filter_by(courseCode=check_course).first()

    if(find_course):
        user_course = Skills(courseCode=check_course, courseSkills=find_course.competencyOutcome, userId=current_user.id)
        db.session.add(user_course)
        db.session.commit()
        return redirect(url_for('profile_views.get_user_page')) 
    else:
        flash('course not in our database!')
        return redirect(url_for('profile_views.get_user_page'))
    


@profile_views.route('/profile/<id>', methods=['GET'])
@login_required
def delete_course(id):
    course = Skills.query.filter_by(id=id, userId=current_user.id).first()
    if course == None:
        flash ('Invalid id or unauthorized')
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for('profile_views.get_user_page')) 