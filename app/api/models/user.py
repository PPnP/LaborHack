from flask_login import UserMixin

from app import db, login_manager


class User(db.Model, UserMixin):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(10), default='')

    name = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    email = db.Column(db.String(50))
    password = db.Column(db.String(100))

    avatar = db.Column(db.String(300), nullable=True)

    def __init__(self, role, name, phone, email, password):
        self.role = role
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password

    def __repr__(self):
        return 'User {} {}>'.format(self.name, self.email)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=str(user_id)).first()
