from flask import render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_login import current_user

from app.api.controllers.form import FormController
from app.api.forms.help import SubmitApplicationForm


class HelpController(FormController):
    action = '/help'

    def get_form(self) -> FlaskForm:
        return SubmitApplicationForm()

    def get(self):
        user = None
        if current_user.is_authenticated:
            user = current_user
        return render_template('help.html', form=self.get_form(), action=self.action, user=user)

    def process(self, form: FlaskForm):
        flash('Заявка сохранена', 'success')
        return redirect(url_for('api.Help'))
