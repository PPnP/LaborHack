from flask import render_template
from flask.views import MethodView
from flask_login import current_user


class EducationController(MethodView):
    def get(self):
        user = None
        if current_user.is_authenticated:
            user = current_user
        return render_template('education.html', user=user)
