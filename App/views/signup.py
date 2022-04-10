from flask import Blueprint, redirect, render_template, request, flash, url_for
#from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from App.database import db
from App.forms import SignUp
from App.models import User


signup_views = Blueprint('signup_views', __name__, template_folder='../templates')

@signup_views.route('/signup', methods=['GET'])
def get_signup_docs():
    form=SignUp()
    return render_template('signup.html', form=form)

@signup_views.route('/signup', methods=['POST'])
def signupUser():
    form = SignUp()
    if form.validate_on_submit():
        data = request.form
        comparison = User.query.filter_by(email=data['email']).first()
        if comparison:
            flash('email already exist')
            return redirect(url_for('signup_views.signupUser'))
        newuser = User(username=data['username'], email=data['email'], password=data['password'])
        db.session.add(newuser)
        db.session.commit()
        flash('Account Created!')
        return redirect(url_for('api_views.get_login_page'))  
    flash('Error invalid input!')
    return redirect(url_for('signup_views.signupUser'))