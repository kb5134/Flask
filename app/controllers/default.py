from cgi import print_form
from flask import render_template
from app import app
from app.models.form import LoginForm

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
def teste():
    return render_template('teste crud')