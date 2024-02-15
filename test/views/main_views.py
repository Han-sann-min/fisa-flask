from flask import Blueprint, session, g
from ..models import Question, User
from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix="/")

@bp.route("/", defaults={"name":""})
@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/bye")
def bye():
    return f"main 에서 작성한 bye from : {__name__}"

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)