from flask import Blueprint, render_template
from flask_login import login_required, current_user

blueprint = Blueprint(
    'realm', 
    __name__, 
    template_folder='../../data/html'
)

@blueprint.route('/select-realm', methods=['GET'])
@login_required
def select_realm():

    available_realms = [
        {'id': 3, 'name': 'Realm 3', 'population': 100},
        {'id': 4, 'name': 'Realm 4', 'population': 200},
    ]
    return render_template(
        'select_realm.html', 
        user=current_user, 
        available_realms=available_realms
    )
