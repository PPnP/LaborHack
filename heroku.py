from app import application
from app.api import routes
from manage import db_reset


db_reset()
application.config['DOMAIN'] = ''  # fill it
application.register_blueprint(routes.api, url_prefix='/')


if __name__ == '__main__':
    application.run()
