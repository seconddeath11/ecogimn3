import os

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = os.environ['USERNAME']
MAIL_PASSWORD = os.environ['PASSWORD']
SECRET_STRING = os.environ['SECRET_STRING']
MAIL_USE_TLS = False
MAIL_USE_SSL = True
