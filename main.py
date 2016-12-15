#!./env/bin/python

from flask import Flask, jsonify
import flask_login

import helper

app = Flask('application')

app.config['SECRET_KEY'] = 'secret stuff'

# Login Manager
app.login_manager = flask_login.LoginManager()
app.login_manager.init_app(app)
app.login_manager.login_view = 'login'


class Account(flask_login.UserMixin):

    def __init__(self, email):
        self.email = email

    def get_id(self):
        return self.email

user = Account(email='me@example.com')

accounts_by_email = {user.email: user}


@app.login_manager.user_loader
def load_user(email):
    return accounts_by_email.get(email)


@app.route('/')
def home():
    return jsonify('Hello world')


@app.route('/login')
def login():
    flask_login.login_user(user)
    return jsonify()


@app.route('/check')
@flask_login.login_required
def check():
    print 'Email: ' + flask_login.current_user.email
    helper.do_thing(flask_login.current_user)
    return jsonify(user.email)




