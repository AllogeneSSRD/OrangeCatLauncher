#
# @file models.py
# 模型

from datetime import datetime

from exts import db

class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, unique=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    pwd = db.Column(db.String(128))
    email = db.Column(db.String(128), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)
    abled = db.Column(db.Boolean, default=True)
    ban = db.Column(db.Boolean, default=False)
    activity = db.Column(db.Integer, default=1)
    member = db.Column(db.String(64), default="用户")
    level = db.Column(db.Integer, default=0)
    login = db.Column(db.Boolean, default=True)
    login_duration = db.Column(db.Integer)

class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), nullable=False)
    captcha = db.Column(db.String(16), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)
    # used = db.Column(db.Boolean, default=False)