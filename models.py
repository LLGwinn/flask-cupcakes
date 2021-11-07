"""Models for Cupcake app """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """ Connect to database """

    db.app = app
    db.init_app(app)

# https://tinyurl.com/yxrua4jp

class Cupcake(db.Model):

    __tablename__ = 'cupcakes'

    id = db.Column( 
        db.Integer, 
        primary_key=True, 
        autoincrement=True 
    )

    flavor = db.Column( 
        db.Text, 
        nullable=False, 
        unique=True 
    )

    size = db.Column( 
        db.Text, 
        nullable=False 
    )

    rating = db.Column( 
        db.Float, 
        nullable=False 
    )

    image = db.Column(
        db.Text,
        nullable=False,
        default='https://tinyurl.com/demo-cupcake'
    )

