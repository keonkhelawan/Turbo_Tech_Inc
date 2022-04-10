from flask import Blueprint, render_template
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
list_views = Blueprint('list_views', __name__, template_folder='../templates')

from App.models import Job

@list_views.route('/list', methods=['GET'])
def get_user_page():
    list_of_jobs = Job.query.all()
    return render_template('list.html', jobData=list_of_jobs)