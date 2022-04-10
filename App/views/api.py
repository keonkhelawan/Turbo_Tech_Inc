from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import login_user
from App.database import db
from App.forms import LogIn
from App.models import User

api_views = Blueprint('api_views', __name__, template_folder='../templates')

@api_views.route('/', methods=['GET'])
def get_login_page():
    form = LogIn()
    return render_template('login.html', form=form)

@api_views.route('/', methods=['POST'])
def login_current_user():
    form = LogIn()
    if form.validate_on_submit():
        data = request.form
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            flash('Logged in successfully.')
            login_user(user)
            return redirect(url_for('profile_views.get_user_page'))
    flash('Invalid credentials')
    return redirect(url_for('api_views.login_current_user'))        