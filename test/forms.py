                
## forms.py
from flask_wtf import FlaskForm
from flask import g
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
	# 화면에서 출력할 해당 필드의 라벨, 필수 항목 체크 여부s
    subject = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])
    
class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])
    
class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=5, max=25, message="ID 는 5글자 이상 25글자 이하여야 합니다.")])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])


class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=5, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])
