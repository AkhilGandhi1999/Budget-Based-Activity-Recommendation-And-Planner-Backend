import functools

from flask import (
    Blueprint
)

bp = Blueprint('categories', __name__, url_prefix='/categories')

@bp.route('/get_categories', methods=('GET', 'POST'))
def recommend():
    
    return "you reached categories"
