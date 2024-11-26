from flask import Blueprint, render_template
from flask_login import login_required, current_user

blueprint = Blueprint('dashboard', __name__, template_folder='../../data/html/dashboard')

@blueprint.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)
