from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import  login_required, current_user
from App.models import Course
from App.database import db
from App.controllers import capital_letter

profile_views = Blueprint('profile_views', __name__, template_folder='../templates')

@profile_views.route('/profile', methods=['GET'])
@login_required
def get_user_page():
    course = course = Course.query.filter_by(userId=current_user.id).all()
    return render_template('profile.html', courses=course)


@profile_views.route('/profile', methods=['POST'])
@login_required
def update_user_page():
    data = request.form['text']

    check_course = capital_letter(data)
    if (check_course == "error"):
        flash('not a valid course code')
        return redirect(url_for('profile_views.get_user_page'))

    duplicate = Course.query.filter_by(courseCode=check_course).first()
    if duplicate:
        flash('course already in list')
        return redirect(url_for('profile_views.get_user_page')) 

    course = Course(courseCode=check_course, userId=current_user.id)
    db.session.add(course)
    db.session.commit()
    return redirect(url_for('profile_views.get_user_page')) 


@profile_views.route('/profile/<id>', methods=['GET'])
@login_required
def delete_course(id):
    course = Course.query.filter_by(courseId=id, userId=current_user.id).first()
    if course == None:
        flash ('Invalid id or unauthorized')
    db.session.delete(course)
    db.session.commit()
    flash ('course deleted!')
    return redirect(url_for('profile_views.get_user_page')) 