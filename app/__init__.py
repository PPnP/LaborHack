from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_mail import Mail, Message
from threading import Thread


application = Flask(__name__, template_folder='./templates', static_folder='./static')
application.config.from_object('config')

manager = Manager(application)

db = SQLAlchemy(application)
migrate = Migrate(application, db)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(application)
login_manager.login_message_category = 'info'
login_manager.login_message = 'Данный раздел требует авторизации.</br>Пожалуйста, войдите или зарегистрируйтесь.'
login_manager.login_view = 'api.Login'

mail = Mail(application)


def asynchronous(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


@asynchronous
def send_async_email(msg):
    with application.app_context():
        mail.send(msg)


def send_email(subject, recipients, html):
    msg = Message(subject, recipients=recipients)
    msg.html = html
    send_async_email(msg)
