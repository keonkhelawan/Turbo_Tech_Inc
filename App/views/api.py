from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.database import db
from App.models import Job

api_views = Blueprint('api_views', __name__, template_folder='../templates')

@api_views.route('/', methods=['GET'])
def get_api_docs():
    list_of_jobs = Job.query.all()
    return render_template('index.html', jobData=list_of_jobs)