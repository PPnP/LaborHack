from app.api.forms import *


class SubmitApplicationForm(FlaskForm):
    name = StringField(label='Имя и фамилия', validators=[InputRequired(message='Заполните все обязательные поля')])
    phone = StringField(label='Телефон', validators=[InputRequired(message='Заполните все обязательные поля')])
    comment = StringField(label='Ваше сообщение', validators=[InputRequired(message='Заполните все обязательные поля')])
    is_anonymous = BooleanField(label='Анонимно', validators=[InputRequired(message='Заполните все обязательные поля')])
    submit = SubmitField('Отправить')
