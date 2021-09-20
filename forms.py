from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms import MultipleFileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileField


class Form(FlaskForm):
    username = StringField('ФИО', validators=[DataRequired()])
    school = SelectField('Школа', choices=[('Гимназия 3', 'Гимназия 3'), ('СШ №11', 'СШ №11')])
    class_no = IntegerField('Номер класса', validators=[DataRequired()])
    class_letter = SelectField('Буква класса', choices=[('А', 'A'), ('Б', 'Б')])
    remember = BooleanField('Согласие на ')
    photo = MultipleFileField('Прикрепить фото')
    submit = SubmitField('Отправить')
