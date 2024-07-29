# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class MeatProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    buying_price = FloatField('Buying_price', validators=[DataRequired()])
    selling_price = FloatField('Selling_price', validators=[DataRequired()])
    submit = SubmitField('Add Product')
