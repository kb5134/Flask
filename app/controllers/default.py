from cgi import print_form
import re
from flask import render_template
from app import app, db
from app.models.form import LoginForm
from app.models.tables import User

@app.route('/index/<user>')
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print (form.errors)
    return render_template('login.html', form=form)



@app.route('/teste/<info>')
@app.route('/teste', defaults={'info': None})
def teste(info):
    i = User("allef3", "1234", "teste3", "teste2@allef.com")
    db.session.add(i)
    db.session.commit()
    return "ok"