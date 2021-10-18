import os

from flask_mail import Message


def send_email(form, mail, actions):
    msg = Message(
        "Новое дело",
        sender=os.getenv('USERNAME'),
        recipients=["ecogimn@bk.ru"])
    msg.body = form.username.data + "\n Сделали: " + actions[int(form.actions.data) - 1][
        1] + "\n Школа и класс: " + str(dict(form.school.choices)[form.school.data]) + ", " + str(
        form.class_no.data) + str(form.class_letter.data) + "\n Согласие по фото: " + str(form.remember.data)

    if form.photo.data:
        for ph in form.photo.data:
            msg.attach(
                ph.filename,
                'application/octect-stream',
                ph.read())
    mail.send(msg)


def send_question(form, mail):
    msg = Message(
        "Новый вопрос по теме " + form.subject.data,
        sender=os.getenv('USERNAME'),
        recipients=["ecogimn@bk.ru"])
    msg.body = "имя: " + form.name.data + "\nпочта: " + form.email.data + "\nвопрос: " + form.message.data
    mail.send(msg)
