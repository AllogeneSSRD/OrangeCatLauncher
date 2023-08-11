# coding=utf-8

from __future__ import annotations
import sys  
sys.path.append(".")

from flask import Flask
from flask import render_template as rt
from flask_migrate import Migrate

import config
import time_transform as ttf
from exts import db, mail
from models import UserModel
from blueprints.index import bp as index_bp
from blueprints.auth import bp as auth_bp

app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)
# 先创建后绑定，不需要在创建时绑定
db.init_app(app)
mail.init_app(app)
# 模型映射到数据库
migrate = Migrate(app, db)
# 注册蓝图
app.register_blueprint(index_bp)
app.register_blueprint(auth_bp)
"""迁移三步
flask db init (只需要执行一次)
flask db migrate 将orm模型生成迁移脚本
flask db upgrade 将迁移脚本映射到数据库中
"""


# @app.route("#")
# def test():
#     pass


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
