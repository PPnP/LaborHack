from flask import redirect, url_for, flash
from flask.views import MethodView


class IndexController(MethodView):
    def get(self):
        flash('Оставайтесь дома. В связи с неблагоприятной эпидемиологической обстановкой '
              'постарайтесь не выходить на улицу без необходимости. Это важно 🙂', 'info')
        return redirect(url_for('api.Locations'))
