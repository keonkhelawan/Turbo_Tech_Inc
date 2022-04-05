from flask import Blueprint, render_template
signup_views = Blueprint('signup_views', __name__, template_folder='../templates')

@signup_views.route('/signup', methods=['GET'])
def get_user_page():
    return render_template('signup.html')