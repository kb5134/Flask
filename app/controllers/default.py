from curses import flash
from flask import render_template, flash
from app import app
from app.models.form import LoginForm
from app.models.tables import User
from flask_login import login_user


@app.route('/index/<user>')
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("logado")
        else:
            flash('Login Invalido')
    else:
        print (form.errors)
    return render_template('login.html', form=form)

