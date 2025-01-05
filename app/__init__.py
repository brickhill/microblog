# Flask App package.
# 04.01.2025

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# print(app.config)

from app import routes
