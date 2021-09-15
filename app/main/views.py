from flask import render_template, flash, request, url_for, redirect, jsonify, session
from flask_login import current_user, login_required
from sqlalchemy.sql.expression import func

from ..models import Question
from . import main 
from .forms import QuestionForm, HomeForm
from .. import db
from ..decorators import admin_required

from flask_nav.elements import View, Navbar, Separator
from app import nav

@main.before_app_first_request
def main_navbar():
    main_navbar = Navbar('Quick Test',
        View('Home', 'main.index'),
        View('About', 'main.about'),
        View('Logout', 'auth.logout')) 
    return main_navbar

nav.register_element('main_navbar', main_navbar)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = HomeForm()
    if form.validate_on_submit():
        session['subjectid'] = form.subject.data
        session['per_page'] = form.questions_per_page.data
        session['randomize'] = form.random.data
        return redirect(url_for('.questionform'))
    return render_template('index.html', form = form)

@main.route('/questions')
@login_required
def questionform():
    page = request.args.get('page', 1, type=int)
    subjectid = session['subjectid']
    per_page = session['per_page']
    randomize = session['randomize']
    if randomize == True:
        pagination = Question.query.filter_by(subject_id=subjectid).order_by(func.random()).paginate(
            page, per_page=per_page, error_out=False)
    else:
        pagination = Question.query.filter_by(subject_id=subjectid).order_by(Question.id).paginate(
            page, per_page=per_page, error_out=False)
    questions = pagination.items
    return render_template('questionform.html', questions=questions, pagination=pagination)

@main.route('/update', methods=['POST'])
@login_required
def update():
    question = Question.query.filter_by(id=request.form['question_id']).first()
    choice = request.form['choice']
    choice_id = str(question.id)+choice

    if choice == question.answer:
        message = 'Correct'
        return jsonify({'answer' : question.answer, 'choice_id': choice_id, 'id': question.id})

    return jsonify({'error': 'wrong answer', 'choice': choice, 'choice_id': choice_id})

@main.route('/addq', methods=['GET', 'POST'])
@login_required
@admin_required
def addquestionform():
    form = QuestionForm()
    if form.validate_on_submit():
        last_id_query = Question.query.order_by(Question.id.desc()).first()
        if last_id_query == None:
            last_id = 0
        else:
            last_id = last_id_query.id
        question = form.question.data
        choices = form.choices.data
        tostring = choices.strip().replace(',', ';').replace('\n', ', ').replace('\r', '')
        subject = form.subject.data
        answer = form.answer.data
        question = Question(id = last_id+1, question=question.replace('\n', ' ').replace('\r', ''), choices=tostring, 
            answer=answer, subject_id=subject)
        db.session.add(question)
        db.session.commit()
        flash('Question Submitted')
        return redirect(url_for('.addquestionform'))
    return render_template('addquestion.html', form=form)
