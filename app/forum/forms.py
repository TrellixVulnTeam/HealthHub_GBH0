from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, TextField, TextAreaField#,DateField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo, NumberRange
from wtforms import ValidationError
from wtforms.fields.html5 import DateField
from wtforms_components import DateRange
from datetime import datetime, date
from .. import db
from ..models import User, Hospital
from wtforms.widgets.core import html_params
from wtforms.widgets import HTMLString

class PostForm(FlaskForm):
    text = TextAreaField('Post', validators = [Required(), Length(10,250)])
    submit = SubmitField('Post')
