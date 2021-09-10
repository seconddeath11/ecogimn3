from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms import MultipleFileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileField


class Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    school = SelectField(choices=[('Гимназия 3', 'Гимназия 3'), ('СШ №11', 'СШ №11')])
    class_no = StringField('class_no', validators=[DataRequired()])
    class_letter = SelectField(choices=[('А', 'A'), ('Б', 'Б')])
    remember_me = BooleanField('Remember Me')
    photo = MultipleFileField()
    submit = SubmitField('Sign In')
