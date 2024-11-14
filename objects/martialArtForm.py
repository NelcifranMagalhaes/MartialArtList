from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, IntegerField

class MartialArtForm(FlaskForm):
    name = StringField("Martial Art's name", [validators.DataRequired(), validators.Length(min=1, max=50)])
    category = StringField('Category', [validators.DataRequired(), validators.Length(min=1, max=40)])
    points = IntegerField('Points', [validators.DataRequired(), validators.NumberRange(min=1, max=10)])
    save = SubmitField('Save')