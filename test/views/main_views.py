from flask import Blueprint
from ..models import Question
bp = Blueprint('main', __name__, url_prefix="/")

@bp.route("/", defaults={"name":""})
@bp.route("/<string:name>")
def hello(name):
    return f"main 에서 작성한 hello from : {name}"

@bp.route("/bye")
def bye():
    return f"main 에서 작성한 bye from : {__name__}"