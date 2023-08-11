#
# @file space.py
# 登录 授权

# import sys  
# sys.path.append("...")

# import string
import sys
import random
from typing import Callable

from flask import Blueprint
from flask import request, jsonify, redirect, url_for, session
from flask import render_template as rd
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

from exts import db, mail
from models import UserModel
from models import EmailCaptchaModel
import time_transform as ttf

from .forms import RegisterForm, LoginForm

bp = Blueprint("space", __name__, url_prefix="/space")

time = ttf.timedict

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return rd("/login.html")
    elif request.method == "POST":
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()

            if not user:
                print("登录失败，邮箱未注册~")
                return redirect(url_for("space.login"))
            
            elif check_password_hash(user.password, password):
                print("登录成功！")
                # cookie 存放少量auth数据
                # flask中的session即以加密数据存储在cookie中
                session["user_id"] = user.id
                return redirect("/")

            else:
                print("登录失败，邮箱或密码错误~")
                return redirect(url_for("space.login"))
        else:
            print(form.errors)
            return redirect(url_for("space.login"))
        
    return rd("login.html")# "这是登录页面"

# 使用methods以外的请求报405错误
@bp.route("/register", methods=["GET", "POST"])
def register() -> str:
    if request.method == "GET":
        return rd("/register.html")
    
    elif request.method == "POST":
        # 表单验证: flask-wtf
        form = RegisterForm(request.form)

        if form.validate():# validate会自动调用class中的验证器和自定义函数 返回bool
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username,
                             password=generate_password_hash(password),
                             pwd=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("space.login"))
        # f"注册成功！点击返回以跳转<br>success {__name__}<br>function {sys._getframe().f_code.co_name}"
        else:
            print(form.errors)
            return redirect(url_for("space.register"))
        # f"注册失败！点击返回以重新输入<br>fail {__name__}<br>function {sys._getframe().f_code.co_name}"

# bp.route: 如果木有指定methods参数，默认GET请求
@bp.route("/captcha/email")
def get_email_captcha() -> jsonify:
    # /captcha/email<email>
    # /captcha/email?email=xxx@qq.com
    email = request.args.get("email")
    # 验证码：4/6位 随机数字/字母/组合
    # string.digits*4
    source = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    captcha = "".join(random.sample(source, 4))
    body = "Hi,亲爱的\n\n您于 "+time["Y"]+"年"+time["m"]+"月"+time["d"]+"日 "+time["week_cn"]+" "\
        +time["H"]+":"+time["M"]+":"+time["S"]+" "+time["p"]\
        +f" 通过电子邮箱在 [猫猫窝] 进行注册。\n\n\
        如果是您本人，请使用以下验证码验证您的电子邮箱: {captcha} \n\n\
        请勿泄露或转发。\n\n\
        如果您收到多封邮件，请以最后一封邮件为准。\n\n\
        如果您没有注册过 [猫猫窝] ，您可以忽略这封邮件。\n\n\
        谢谢 from  一般路过千秋九"
    message = Message(subject="[橘猫猫]：请验证您的电子邮箱", recipients=[email], body=body)
    mail.send(message)
    # memcached/redis
    # 数据库表
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()

    print("验证码 "+captcha)
    # RESTful API
    # {code: 200/400/500, msg: "", data: {}}
    return jsonify({
        "code": 200,
        "msg": "",
        "data": None
    })

# @bp.route("/mail/test")
# def mail_test():
#     message = Message(subject="邮箱测试",
#                       recipients=["SSRD_2022@outlook.com"], body="这是一条测试邮件")
#     mail.send(message)
#     return "邮件发送成功！"