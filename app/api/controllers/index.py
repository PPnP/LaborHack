from flask import redirect, url_for, flash
from flask.views import MethodView


class IndexController(MethodView):
    def get(self):
        return redirect(url_for('api.Locations'))
