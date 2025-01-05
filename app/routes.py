# Flask App routes.
# 04.01.2025

from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Peter"}
    posts = [
        {"author": {"username": "Peter"}, "body": "Post number 1"},
        {"author": {"username": "Frank"}, "body": "Post number 2"}
    ]
    return render_template("index.html", title=None, user=user, posts=posts)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for user {} remember_me ={}'.format(form.username.data,
        form.remember_me.data))
        return redirect(url_for('index'))
    return render_template("login.html", title="Login", form=form)