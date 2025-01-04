# Flask App package.
# 04.01.2025

from flask import Flask

app = Flask(__name__)

from app import routes
