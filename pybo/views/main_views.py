from flask import Blueprint, url_for, current_app 
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'



@bp.route('/')
def index():
    current_app.logger.info("INFO 레벨로 출력")
