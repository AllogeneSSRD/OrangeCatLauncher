#
# @file config.py
# 配置

# 数据库配置
HOSTNAME = "127.0.0.1"
PORT = "3306"
DATABASE = "orangecat_launcher"
USERNAME = "root"
PASSWORD = "root"
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "1252231934@qq.com"
MAIL_PASSWORD = "xhzbtfnqminnjdha"
MAIL_DEFAULT_SENDER = "1252231934@qq.com"

# cookie 配置
SECRET_KEY = "f67YU78dr6G878gC"