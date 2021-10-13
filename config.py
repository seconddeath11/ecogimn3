import os

from boto.s3.connection import S3Connection
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = S3Connection(os.environ['USERNAME'])
MAIL_PASSWORD = S3Connection(os.environ['PASSWORD'])
MAIL_USE_TLS = False
MAIL_USE_SSL = True
