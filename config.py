import os

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = os.environ['USERNAME']
MAIL_PASSWORD = os.environ['PASSWORD']
SECRET_KEY = os.environ['SECRET_KEY']
MAIL_USE_TLS = False
MAIL_USE_SSL = True
