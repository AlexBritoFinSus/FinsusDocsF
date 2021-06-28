from flask import Flask, render_template, request, redirect, url_for, abort
from flask_login import LoginManager, logout_user, current_user, login_user, login_required
from flask_sqlalchemy import SQLAlchemy
from werkzeug.urls import url_parse

from forms import LoginForm
# import bcrypt
# import pyodbc


app = Flask(__name__)
app.config['SECRET_KEY'] = '2150f8f70f8c2acdd3f713e26a7fce24b6684486f83772f2b85489394bac16d655c2837dd0075e4cee53474ff7c37d8ad453f67a0f6f1e4b0a5eae6af2b51a969a3a705e7df96607c160a781c8cbb755e6c3d4add6810a34ed3fb51f91857a81a95d549c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:testing@localhost:5432/bi-finsus'
# params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=bi-finsus.database.windows.net;DATABASE=bi-finsus;UID=samuel;PWD=Adminfinsus1")
# app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager(app)
login_manager.login_view = "login"

db = SQLAlchemy(app)

from models import Usuarios



@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuarios.get_by_email(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('pages/login.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    return Usuarios.get_by_id(int(user_id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('/'))


@app.route('/dashboard')
def index():
    return render_template("pages/dashboard.html")

if __name__ == '__main__':
    app.run(debug=True)
