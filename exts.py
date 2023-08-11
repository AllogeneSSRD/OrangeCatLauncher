#
# @file exts.py
# 第三方插件

# 向 app, model 分发 db 解决循环引用

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()