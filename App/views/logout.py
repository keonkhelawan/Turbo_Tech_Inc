from flask_login import login_required, logout_user
from flask import Blueprint, redirect, url_for

logout_views = Blueprint('logout_views', __name__, template_folder='../templates')

@logout_views.route('/logout', methods=['GET'])
@login_required
def logout():
  logout_user()
  return redirect(url_for('api_views.get_login_page')) 