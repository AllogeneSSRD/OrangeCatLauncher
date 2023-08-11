#
# @file forms.py
# 验证

import wtforms as wtf
from wtforms.validators import Email as Email
from wtforms.validators import Length, EqualTo
from wtforms.validators import ValidationError as WtfValidationError

from exts import db
from models import UserModel, EmailCaptchaModel


class ValidationError(WtfValidationError):
    pass

class FormLength():
    """
    init继承源
    """
    def __init__(self, min=-1, max=-1, message=None):
        assert (
            min != -1 or max != -1
        ), "At least one of `min` or `max` must be specified."
        assert max == -1 or min <= max, "`min` cannot be more than `max`."
        self.min = min
        self.max = max
        self.message = message
        self.field_flags = {}
        if self.min != -1:
            self.field_flags["minlength"] = self.min
        if self.max != -1:
            self.field_flags["maxlength"] = self.max

    def __call__(self, form, field):
        length = field.data and len(field.data) or 0
        if length >= self.min and (self.max == -1 or length <= self.max):
            return

        if self.message is not None:
            msg = self.message

        elif self.message is None:
            msg = "Flied"

        if self.max == -1:
            message = f"{msg} must be at least {self.min} character long."
        
        elif self.min == -1:
            message = f"{msg} cannot be longer than {self.max} character."

        elif self.min == self.max:
            message = f"{msg} must be exactly {self.max} character long."

        else:
            message = f"{msg} 长度必须在 {self.min} - {self.max} 之间，可以使用Unicod字符"

        raise ValidationError(message % dict(min=self.min, max=self.max, length=length))


# Form: 验证前端提交数据
class RegisterForm(wtf.Form):
    email = wtf.StringField(validators=[Email(message="邮箱格式错误！")])
    captcha = wtf.StringField(validators=[Length(min=4, max=4, message="验证码长度应为4位！")])
    username = wtf.StringField(validators=[FormLength(min=3, max=30, message="用户名")])
    password = wtf.StringField(validators=[Length(min=6, max=30, message="密码应为6~30个字符~")])
    password_confirm = wtf.StringField(validators=[EqualTo("password", message="两次输入的密码不同！")])
    # password_confirm = wtf.StringField(validators=[EqualTo("password", message="两次密码不一致！")])
    
    # 自定义验证 
    # 1. 邮箱是否已被注册
    def validate_email(self, field):
        email = field.data
        email_used = UserModel.query.filter_by(email=email).first()
        if email_used:
            print(f"{email}邮箱已被注册")
            raise wtf.ValidationError(message="该邮箱已被注册~")
        
        
    # 2. 验证码是否正确
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_verify = EmailCaptchaModel.query.filter_by(email=email, captcha=captcha).first()
        if not captcha_verify:
            raise wtf.ValidationError(message="验证码错误~")
        # To do: 可以去数据库删掉captcha_y
        # to do: 此处功能如果酮个邮箱，发送多次注册，应该取最后一个。
        # else:
        #     # 在这里清理数据会占用不必要的数据库性能
        #     # 建议写个脚本每日删库即可
        #     db.session.delete(captcha_verify)
        #     db.session.commit()
        #     print(f"{email}验证成功{captcha}|{captcha_verify}，已删库")


class LoginForm(wtf.Form):
    
    email = wtf.StringField(validators=[Email(message="邮箱格式错误！")])
    # username = wtf.StringField(validators=[FormLength(min=3, max=30, message="用户名")])
    password = wtf.StringField(validators=[Length(min=6, max=30, message="密码应为6~30个字符~")])