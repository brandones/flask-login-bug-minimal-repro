#!./env/bin/python

from flask import Flask, jsonify
import flask_login
from google.appengine.ext import ndb

import helper

app = Flask('application')

app.config['SECRET_KEY'] = 'secret stuff'

# Login Manager
app.login_manager = flask_login.LoginManager()
app.login_manager.init_app(app)
app.login_manager.login_view = 'login'


class Account(ndb.Model, flask_login.UserMixin):
    email = ndb.StringProperty()
    is_active = ndb.BooleanProperty(default=True)

    def get_id(self):
        return self.key.id()

user = Account(email='me@example.com')
user.put()


@app.login_manager.user_loader
def load_user(user_id):
    return Account.get_by_id(user_id)


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




