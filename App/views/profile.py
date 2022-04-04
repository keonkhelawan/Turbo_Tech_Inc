from flask import Blueprint, render_template
profile_views = Blueprint('profile_views', __name__, template_folder='../templates')

@profile_views.route('/profile', methods=['GET'])
def get_user_page():
    return render_template('profile.html')

    