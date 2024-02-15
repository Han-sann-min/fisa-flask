from flask import Blueprint, render_template, url_for, redirect, request, session, g, flash
from ..models import Question, Answer, User
from ..forms import QuestionForm, AnswerForm
from test import db
from test.models import Question
from datetime import datetime
from test.views.auth_views import login_required
board = Blueprint('board', __name__, url_prefix="/board")

# @board.route("/list")
# def post_list():
#     question_list=Question.query.all()
#     return render_template("question/question_list.html", question_list=question_list)

@board.route("/list")
def post_list():
    page = request.args.get("page", type=int, default=1)
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page=page,per_page=10)
    return render_template("question/question_list.html", question_list=question_list)


@board.route("/detail/<int:question_id>") 
def post_detail(question_id):
    # question = Question.query.filter_by(id=question_id).first()
    question = Question.query.get_or_404(question_id)
    form = AnswerForm()
    return render_template("question/question_detail.html", question=question, form=form, question_id=question_id)

@board.route("/create", methods=["GET", "POST"])
@login_required
def create():
    # 폼을 받는다
    form = QuestionForm(csrf_enabled=True)
    # 폼에 온 양식이 우리가 forms.py 에 작성한 양식과 일치하는지 확인하기
    if form.validate_on_submit():
        ## flask shell
        q = Question(user_id=g.user.id, subject=form.subject.data, content=form.content.data, create_date=datetime.now())                                                       
        db.session.add(q)         
        db.session.commit()
        return redirect( url_for('board.post_list'))

    return render_template("question/question_form.html", form=form)

@board.route("/modify/<int:question_id>", methods=("GET", "POST")) 
@login_required
def modify(question_id):
    question = Question.query.get_or_404(question_id)
    if g.user != question.user :
        flash("수정 권한이 없습니다.")
    if request.method == "POST":
        form = QuestionForm()
        if form.validate_on_submit():
            form.populate_obj(question) # 화면에 원래 DB 에서 꺼낸 값을 뿌려줌
            db.session.commit()
            return redirect( url_for("board.post_detail", question_id=question_id))
    else :
        form = QuestionForm(obj=question)
    return render_template("question/question_form.html", form=form)

@board.route("/delete/<int:question_id>", methods=('GET', 'POST'))
@login_required
def delete(question_id):
    # 글을 가져옴
    question = Question.query.get_or_404(question_id)
    # 현재 접속한 사용자와 글의 작성자가 일치하는지 확인
    if g.user != question.user :
        flash("삭제 권한이 없습니다.")
        return redirect(url_for("board.post_detail", question_id=question_id))
        # 일치하지 않으면 -> 삭제권한이 없습니다 메시지 출력
        # 원래 글로 되돌아감
    else :
        db.session.delete(question)
        db.session.commit()
        return redirect(url_for("board.post_list"))
    
    # db.session.delete(글)
    #커밋
    # question_list로 되돌아감 