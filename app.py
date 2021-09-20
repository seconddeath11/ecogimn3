import json

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from werkzeug.utils import redirect

from forms import Form
from mail import send_email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'
bootstrap = Bootstrap(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = USERNAME
app.config['MAIL_PASSWORD'] = PWD
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/")
def index():
    with open('static/pins.json', encoding='utf-8') as json_file:
        pins = json.load(json_file)

    return render_template("index.html", len=len(pins['station']), pins=pins['station'])


@app.route('/form', methods=['GET', 'POST'])
def login():
    form = Form()
    if form.validate_on_submit():
        send_email(form, mail)
        return redirect('/success')
    print(form.errors)
    return render_template('form.html', form=form)


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/results")
def results():
    return render_template("results.html")


if __name__ == "__main__":
    app.run()
