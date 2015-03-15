from flask import Flask, jsonify, render_template, flash, session, url_for, request
from wtforms import Form
from flask_bootstrap import Bootstrap
from flask import redirect
from werkzeug.contrib.fixers import ProxyFix
# from flask_login import login
from flask.ext.login import LoginManager, login_user, logout_user, login_required
import forms
import user


app = Flask(__name__)
app.config.from_object('config')
login_manager = LoginManager()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        form = forms.SignupForm(request.form)
        if form.validate():
            return redirect('/')
        else:
            return render_template('signup.html', form = form)
    return render_template('signup.html', form = forms.SignupForm())

@app.route('/data')
@login_required
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)

app.wsgi_app = ProxyFix(app.wsgi_app)

@login_manager.user_loader
def load_user(userid):
    print 'this is executed',userid
    test_user = user.User()
    test_user.username="johndoe"
    return test_user

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'POST':
        form = forms.LoginForm(request.form)
        if form.validate():
            flash("Logged in successfully!")
            form_user = user.User()
            login_user(form_user)
            return redirect('/')
            #login and validate useer
            # login_user(user_name)
        else:
            return redirect(url_for('signup'))
    if request.method == "GET":
        return render_template('login.html', form = forms.LoginForm())

if __name__ == '__main__':
    Bootstrap(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    # dynamo = Dynamo(app)
    app.run(debug=True)