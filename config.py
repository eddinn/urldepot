import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    # Database config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or \
        "you-willnever-guess-the-supersecret-key"
    DEBUG = True
    # WTForms CSRF enable
    CSRF_ENABLED = True
    # Mail config
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # Admin email
    ADMINS = ['no-reply@urldepot.net']
    # Pagination
    POSTS_PER_PAGE = 25
    # Elasticsearch
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    # Servername
    # SERVER_NAME = os.environ.get('SERVER_NAME')
    # Uploads
    UPLOADS_DEFAULT_DEST = '/app/main/static/uploads/'
    UPLOADS_DEFAULT_URL = 'http://localhost:5000/static/uploads/'
    UPLOADED_PDF_DEST = '/app/main/static/uploads/'
    UPLOADED_PDF_URL = 'http://localhost:5000/static/uploads/'
