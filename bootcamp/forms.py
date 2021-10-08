#forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    
    name  = StringField('Name of Puppy: ')
    submit = SubmitField('Add puppy')
    
class DelForm(FlaskForm):
    id = IntegerField('Id number of Puppy to remove')
    submit = SubmitField('Remove puppy')
    