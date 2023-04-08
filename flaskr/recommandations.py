import functools

from flask import (
    Blueprint
)

bp = Blueprint('recommend', __name__, url_prefix='/recommend')

@bp.route('/get_recomandations', methods=('GET', 'POST'))
def recommend():
    
    return "You reached the get"
