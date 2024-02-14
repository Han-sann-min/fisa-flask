from flask import Blueprint
from ..models import Question
from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix="/")

@bp.route("/", defaults={"name":""})
@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/bye")
def bye():
    return f"main 에서 작성한 bye from : {__name__}"