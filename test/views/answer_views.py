from flask import Blueprint, redirect, render_template, url_for
from ..forms import AnswerForm
from test import db
from  ..models import Answer
from datetime import datetime


answer = Blueprint('answer', __name__, url_prefix="/answer")

@answer.route("/create/<int:question_id>", methods=["GET", "POST"])
def create(question_id):
    form = AnswerForm(csrf_enabled=True)
    
    if form.validate_on_submit():
        a = Answer(question_id=question_id, content=form.content.data, create_date=datetime.now())
        db.session.add(a)
        db.session.commit()
        return  redirect (url_for ("board.post_detail", question_id=question_id))
    return render_template("question/question_detail.html", question_id=question_id, form=form)

