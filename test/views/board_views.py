from flask import Blueprint, render_template, url_for, redirect
from ..models import Question, Answer
from ..forms import QuestionForm, AnswerForm
from test import db
from test.models import Question
from datetime import datetime
board = Blueprint('board', __name__, url_prefix="/board")

@board.route("/list")
def post_list():
    question_list=Question.query.all()
    return render_template("question/question_list.html", question_list=question_list)

@board.route("/detail/<int:question_id>") 
def post_detail(question_id):
    # question = Question.query.filter_by(id=question_id).first()
    question = Question.query.get_or_404(question_id)
    form = AnswerForm()
    return render_template("question/question_detail.html", question=question, form=form, question_id=question_id)

@board.route("/create", methods=["GET", "POST"])
def create():
    # 폼을 받는다
    form = QuestionForm(csrf_enabled=True)
    # 폼에 온 양식이 우리가 forms.py 에 작성한 양식과 일치하는지 확인하기
    if form.validate_on_submit():
        ## flask shell
        q = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())                                                       
        db.session.add(q)         
        db.session.commit()
        return redirect( url_for('board.post_list'))

    return render_template("question/question_form.html", form=form)