from flask import Blueprint


api = Blueprint('api', __name__, template_folder='../templates', static_folder='../static')


from app.api.controllers.locations import LocationsController
api.add_url_rule('/', view_func=LocationsController.as_view('Locations'))

from app.api.controllers.desk import DeskController
api.add_url_rule('/desk', view_func=DeskController.as_view('Desk'))

from app.api.controllers.search import SearchController
api.add_url_rule('/search', view_func=SearchController.as_view('Search'))

from app.api.controllers.education import EducationController
api.add_url_rule('/education', view_func=EducationController.as_view('Education'))

from app.api.controllers.help import HelpController
api.add_url_rule('/help', view_func=HelpController.as_view('Help'))

from app.api.controllers.data import DataController
api.add_url_rule('/data/<string:type>', view_func=DataController.as_view('Data'))
