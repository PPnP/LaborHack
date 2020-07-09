from flask import Blueprint


api = Blueprint('api', __name__, template_folder='../templates', static_folder='../static')


from app.api.controllers.index import IndexController
api.add_url_rule('/', view_func=IndexController.as_view('Index'))
