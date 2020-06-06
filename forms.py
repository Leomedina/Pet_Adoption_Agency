from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, SelectField
from wtforms.validators import  InputRequired, Optional,URL

class AddPetForm(FlaskForm):
    """Form for adding pets"""
    name = StringField("Pet Name", validators = [InputRequired()])
    photo_url = StringField("Photo URL", validators = [Optional(), URL()])
    age = IntegerField("Age", validators = [Optional()])
    notes = TextAreaField("Notes", validators = [Optional()])
    species = SelectField("Species", validators = [InputRequired()])

class EditPetForm(FlaskForm):
    name = StringField("Pet Name", validators = [InputRequired()])
    photo_url = StringField("Photo URL", validators = [Optional(), URL()])
    age = IntegerField("Age", validators = [Optional()])
    notes = TextAreaField("Notes", validators = [Optional()])
    species = SelectField("Species", validators = [InputRequired()])