from app.api.forms import *


class ProfileForm(FlaskForm):
    avatar = FileField(label='Аватар')
    profession = StringField(label='Профессия')
    social_networks = StringField(label='Социальные сети')

    file = FileField(label='Фото')
    title = StringField(label='Название')
    date = StringField(label='Дата')

    submit = SubmitField('Изменить')
