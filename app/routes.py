# Flask App routes.
# 04.01.2025

from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Peter"}
    posts = [
        {"author": {"username": "Peter"}, "body": "Post number 1"},
        {"author": {"username": "Frank"}, "body": "Post number 2"}
    ]
    return render_template("index.html", title=None, user=user, posts=posts)

