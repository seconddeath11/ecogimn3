import os

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = os.getenv('USERNAME')
MAIL_PASSWORD = os.getenv('PASSWORD')
SECRET_KEY = os.getenv("SECRET_KEY")
MAIL_USE_TLS = False
MAIL_USE_SSL = True
SERVER_NAME = 'localhost'
