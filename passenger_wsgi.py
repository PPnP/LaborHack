import sys
import os

from app import application
from app.api import routes
from config import MYSQL_USERNAME, MYSQL_PASSWORD, SERVER_IP, MYSQL_PORT, MYSQL_DB_NAME


INTERP = os.path.expanduser('path/to/venv/')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())


application.config['DOMAIN'] = ''  # fill it
application.config['SQLALCHEMY_DATABASE_URI'] = ''.join(
    ['mysql+pymysql://', MYSQL_USERNAME, ':', MYSQL_PASSWORD, '@',
     SERVER_IP, ':', MYSQL_PORT, '/', MYSQL_DB_NAME])
application.register_blueprint(routes.api, url_prefix='/')


if __name__ == '__main__':
    application.run(host='0.0.0.0')
