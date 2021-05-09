from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[
                       InputRequired(message="Pet Name can't be blank")])
    species = SelectField("Species", choices=[
                          ('cat', 'Cat'),  ('dog', 'Dog'),  ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30), Optional()])
    notes = TextAreaField("Notes", validators=[Length(min=15), Optional()])

class EditPetForm(FlaskForm):
    """form editing for existing pet"""
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    notes = TextAreaField("Notes", validators=[Length(min=15), Optional()])
    available = BooleanField('Available?')