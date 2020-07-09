from flask import render_template
from flask.views import MethodView
from flask_login import current_user


class HelpController(MethodView):
    def get(self):
        user = None
        if current_user.is_authenticated:
            user = current_user
        return render_template('help.html', user=user)
