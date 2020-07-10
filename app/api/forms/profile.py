from app.api.forms import *


class AddPortfolioForm(FlaskForm):
    file = FileField(label='Фото', validators=[InputRequired(message='Заполните все обязательные поля')])
    title = StringField(label='Название', validators=[InputRequired(message='Заполните все обязательные поля')])
    date = StringField(label='Дата', validators=[InputRequired(message='Заполните все обязательные поля')])
    submit = SubmitField('Добавить')
