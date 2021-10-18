import json
import os

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from werkzeug.utils import redirect

from forms import SendForm, ContactForm, ResultsForm
from mail import send_email, send_question

app = Flask(__name__)
app.config.from_pyfile('config.py')
bootstrap = Bootstrap(app)
mail = Mail(app)
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


# TODO: check security stuff

# TODO: fix styles for links
@app.route("/")
def index():
    with open(os.path.join(THIS_FOLDER, 'static/pins.json'), encoding='utf-8') as json_file:
        pins = json.load(json_file)

    return render_template("index.html", len=len(pins['station']), pins=pins['station'])


@app.route('/form/<num>', methods=['GET', 'POST'])
def form(num):
    forms = SendForm(class_no=11)
    actions = create_actions()
    forms.actions.choices = actions
    if forms.validate_on_submit():
        send_email(forms, mail, actions)
        return redirect('/success')
    forms.actions.data = num
    return render_template('form.html', form=forms, num=num)


@app.route("/success")
def success():
    return render_template("success.html")


# TODO: add instruction
# TODO: fix styles
@app.route("/rules")
def rules():
    return render_template("rules.html")


@app.route("/pam")
def pam():
    return render_template("pam.html")


# TODO: fix styles
@app.route("/results", methods=['GET', 'POST'])
def results():
    res_form = ResultsForm()
    with open(os.path.join(THIS_FOLDER, 'static/results.json'), encoding='utf-8') as json_file:
        res = json.load(json_file)
    if request.method == 'POST':
        return render_template("results.html", resform=res_form, results=res[res_form.school.data])
    else:
        return render_template("results.html", resform=res_form, results=res['gimn3'])


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form_q = ContactForm()
    if form_q.validate_on_submit():
        send_question(form_q, mail)
        return redirect('/success')
    return render_template('contact.html', form=form_q)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


def create_actions():
    actions = []
    with open(os.path.join(THIS_FOLDER, 'static/pins.json'), encoding='utf-8') as json_file:
        pins = json.load(json_file)
    i = 1
    for pin in pins["station"]:

        for action in pin["actions"]:
            actions.append((i, action))
            i += 1
    return actions
