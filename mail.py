from flask_mail import Message

USERNAME = "stels270799@gmail.com"
PWD = "Polyana764830"


def send_email(form, mail):

    msg = Message(
        form.school.data + " " + form.class_no.data + form.class_letter.data,
        sender=USERNAME,
        recipients=["ecogimn@bk.ru"])
    msg.body = form.username.data + ""
    if form.photo.data:
        for ph in form.photo.data:
            msg.attach(
                ph.filename,
                'application/octect-stream',
                ph.read())
    mail.send(msg)
