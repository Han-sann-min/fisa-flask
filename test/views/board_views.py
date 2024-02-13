from flask import Blueprint, render_template
from ..models import Question
board = Blueprint('board', __name__, url_prefix="/board")

@board.route("/post")
def post_list():
    question_list=Question.query.all()
    return render_template("question_list.html", question_list=question_list)

@board.route("/detail/<int:question_id>") 
def post_detail(question_id):
    # question = Question.query.filter_by(id=question_id).first()
    question = Question.query.get_or_404(question_id)
    if not question:
        pass
    return render_template("question_detail.html", question=question)
   