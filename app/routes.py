# Flask App routes.
# 04.01.2025

from app import app


@app.route("/")
@app.route("/index")
def index():
    return "Nob off"
