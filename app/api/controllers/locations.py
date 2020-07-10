from flask import render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_login import current_user

from config import yandex_api_key
from app.api.controllers.form import FormController
from app.api.forms.event import AddEventForm


class LocationsController(FormController):
    action = '/locations'

    def get_form(self) -> FlaskForm:
        return AddEventForm()

    def get(self):
        user = None
        if current_user.is_authenticated:
            user = current_user
        return render_template('locations.html', form=self.get_form(), action=self.action,
                               yandex_api_key=yandex_api_key, user=user)

    def process(self, form: FlaskForm):
        flash('Мероприятие успешно добавлено', 'success')
        return redirect(url_for('api.Locations'))
