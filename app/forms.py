from flask_wtf import Form
from wtforms import StringField, TextField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = TextField('openid', validators = [DataRequired()])
    remember_me = BooleanField('remember_me', default = False)
