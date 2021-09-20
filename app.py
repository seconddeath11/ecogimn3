import json

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from werkzeug.utils import redirect

from forms import Form
from mail import send_email
# TODO: move config somewhere
USERNAME = "stels270799@gmail.com"
PWD = "Polyana764830"
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
# TODO: check security stuff

# TODO: fix navbar
# TODO: fix styles for links
# TODO: fix position for pins up
# TODO: add instruction
@app.route("/")
def index():
    with open('static/pins.json', encoding='utf-8') as json_file:
        pins = json.load(json_file)

    return render_template("index.html", len=len(pins['station']), pins=pins['station'])


# TODO: check validations
# TODO: add a field
@app.route('/form/<num>', methods=['GET', 'POST'])
def form(num):
    forms = Form()
    if forms.validate_on_submit():
        send_email(forms, mail)
        return redirect('/success')
    print(forms.errors)
    return render_template('form.html', form=forms, num=num)


# TODO: fix styles
@app.route("/success")
def success():
    return render_template("success.html")


# TODO: add results
@app.route("/results")
def results():
    return render_template("results.html")


# TODO: fix styles
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


# TODO: add announcement
if __name__ == "__main__":
    app.run()
