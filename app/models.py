from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
# add anonymous usermixin for future "GUESTS" with no account
from . import db, login_manager

class Subject(db.Model):
    __tablename__ = 'subject'
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(128))
    questions = db.relationship(
        'Question',
        backref='subject',
        lazy='dynamic'
    )

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    question = db.Column(db.Text, unique=True, nullable=False)
    choices = db.Column(db.Text, nullable=False)
    answer = db.Column(db.String(2), nullable=False)
    rationale = db.Column(db.Text)

    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)

    def __repr__(self):
        return '<Question %r>' % self.question

class User_account(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Integer, nullable=False, default=0)

    @property
    def password(self):
        raise AttributeError('Non readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_administrator(self):
        if self.is_admin == 1:
            return True
        else:
            return False
       
    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User_account.query.get(int(user_id))

class AnonymousUser(AnonymousUserMixin):
    def is_administrator(self):
        return False
    
    def is_registered(self):
        return False

login_manager.anonymous_user = AnonymousUser