from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

generic_image = "https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/20183328/Yorkshire-puppy.jpg"

# MODELS BELOW!

class Pet(db.Model):

    __tablename__="pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.text, nullable=False)
    species = db.Column(db.text, nullable=False)
    photo_url = db.Column(db.text)
    age = db.Column(db.integer)
    notes = db.Column(db.text)
    # should be true/false, required, should default to available
    available = db.Column(db.Boolean, nullable=False, default='True')

    def image_url(self):
        """return default image for pet"""
        return self.photo_url or default_image