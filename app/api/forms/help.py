from app.api.forms import *
from wtforms.fields import TextAreaField


class SubmitApplicationForm(FlaskForm):
    comment = TextAreaField(label='Ваше сообщение', validators=[InputRequired(message='Заполните все обязательные поля')])
    is_anonymous = BooleanField(label='Анонимно')
    submit = SubmitField('Отправить')
