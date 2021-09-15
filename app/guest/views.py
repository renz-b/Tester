from flask import render_template, flash, request, url_for, redirect, jsonify, session
from flask_login import current_user
from sqlalchemy.sql.expression import func

from ..models import Question
from . import guest
from .. import db

from flask_nav.elements import View, Navbar, Separator
from app import nav

@guest.before_app_first_request
def guest_navbar():
    guest_navbar = Navbar('Quick Test',
        View('Login', 'auth.login'),
        View('About', 'main.about'))
    return guest_navbar

nav.register_element('guest_navbar', guest_navbar)

@guest.route('/questions')
def questionform():
    question_query = Question.query.order_by(func.random()).limit(5).all()
    questions = question_query
    return render_template('guest/guest_questions.html', questions=questions)

@guest.route('/update', methods=['POST'])
def update():
    question = Question.query.filter_by(id=request.form['question_id']).first()
    choice = request.form['choice']
    choice_id = str(question.id)+choice

    if choice == question.answer:
        message = 'Correct'
        return jsonify({'answer' : question.answer, 'choice_id': choice_id, 'id': question.id})

    return jsonify({'error': 'wrong answer', 'choice': choice, 'choice_id': choice_id})

