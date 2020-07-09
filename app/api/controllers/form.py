from flask import redirect, flash, request
from flask.views import MethodView
from flask_wtf import FlaskForm


class FormController(MethodView):
    def post(self):
        form = self.get_form()
        if form.validate():
            return self.process(form)
        for error in list(form.errors.values()):
            flash(error[0])
        return redirect(request.url)

    def get_form(self) -> FlaskForm:
        raise NotImplementedError('Specify the form')

    def process(self, form: FlaskForm):
        raise NotImplementedError('Specify the action')
