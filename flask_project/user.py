__author__ = 'masawant'
from flask.ext.login import LoginManager, login_user, logout_user, login_required

class User(object):
    username = "Email"
    password = "Password"
    id = "12345"
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return unicode(self.id)
    def __repr__(self):
        return '<User %r>' % (self.username)