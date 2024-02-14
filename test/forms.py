                
## forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
	# 화면에서 출력할 해당 필드의 라벨, 필수 항목 체크 여부s
    subject = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])
    
class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])