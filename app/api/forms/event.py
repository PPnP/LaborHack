from app.api.forms import *


class AddEventForm(FlaskForm):
    title = StringField(label='Название', validators=[InputRequired(message='Заполните все обязательные поля')])
    datetime = StringField(label='Дата и время', validators=[InputRequired(message='Заполните все обязательные поля')])
    location = StringField(label='Место', validators=[InputRequired(message='Заполните все обязательные поля')])
    category = SelectField(label='Категория', choices=[('Досуг', 'Досуг'), ('Религия', 'Религия'), ('Быт', 'Быт'),
                                                       ('Еда', 'Еда'), ('Культура', 'Культура'), ('Развитие', 'Развитие')],
                           validators=[InputRequired(message='Заполните все обязательные поля')])
    submit = SubmitField('Добавить')
