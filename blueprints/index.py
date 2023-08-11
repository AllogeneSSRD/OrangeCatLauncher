#
# @file index.py
# 主页

from flask import Blueprint
from flask import render_template as rd

import time_transform as ttf

bp = Blueprint("index", __name__, url_prefix="/")

# http://127.0.0.1:5000
@bp.route("/")
def index():
    time = ttf.timedict
    return rd("/index.html", time=time)