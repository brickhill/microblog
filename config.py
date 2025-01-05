# Flask config file.
# 05.01.2025

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "None of your business!"
