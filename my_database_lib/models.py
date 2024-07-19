from . import db

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(20))

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "username": self.username
    #     }
