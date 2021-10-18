from flask_wtf import FlaskForm
from wtforms import MultipleFileField, TextAreaField
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Optional

ob = "Это поле обязательно для заполнения"


class SendForm(FlaskForm):
    username = StringField('ФИО', validators=[DataRequired(message=ob)])
    school = SelectField('Школа', choices=[('gimn3', 'Гимназия 3'), ('sc51', 'СШ №11')])
    class_no = SelectField('Номер класса', choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    class_letter = SelectField('Буква класса', choices=[('А', 'A'), ('Б', 'Б'), ('В', 'В'), ('Г', 'Г'), ('Д', 'Д')])
    actions = SelectField('Выбранное действие')
    comment = TextAreaField('Ваш комментарий', validators=[Optional()])
    remember = BooleanField('Согласие на использование информации на сайте гимназии и в группе ВК')
    photo = MultipleFileField('Прикрепить фото', validators=[Optional()])
    submit = SubmitField('Отправить')


class ContactForm(FlaskForm):
    name = StringField("Ваше имя", validators=[DataRequired(message=ob)])
    email = StringField("Ваш email", validators=[DataRequired(message=ob), Email(message="Введите правильный email")])
    subject = StringField("Тема", validators=[DataRequired(message=ob)])
    message = TextAreaField("Ваше сообщение", validators=[DataRequired(message=ob)])
    submit = SubmitField("Отправить")


class ResultsForm(FlaskForm):
    school = SelectField("Выберите вашу школу:", choices=[('gimn3', 'Гимназия 3'), ('sc51', 'СШ №11')])
