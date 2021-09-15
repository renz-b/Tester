from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, AnyOf
from ..models import Question, Subject

class QuestionForm(FlaskForm):
    question = TextAreaField('Question:', validators=[DataRequired()])
    choices = TextAreaField('Choices', validators=[DataRequired()])
    answer = TextAreaField('Answer', validators=[AnyOf(values=['A.', 'B.', 'C.', 'D.', 'E.'], message='Hello')])
    subject = SelectField('Subject', choices=[(1,'General Knowledge'), (2,'Science'),
        (3,'History')], coerce=int)
    submit = SubmitField('Submit')
               
class HomeForm(FlaskForm):
    subject = SelectField('Subject', choices=[(1,'General Knowledge'), (2,'Science'),
        (3,'History')], coerce=int)
    questions_per_page = SelectField('Questions per page', choices=[1,3,5,10,15,25,50], coerce=int)
    random = BooleanField('Randomize?')
    submit = SubmitField('Submit')
    
