from wtforms import StringField, SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class Formulario(FlaskForm):
    a = IntegerField('Valor de A', validators=[DataRequired()])
    b = IntegerField('Valor de B', validators=[DataRequired()])
    c = IntegerField('Valor de C', validators=[DataRequired()])
    enviar = SubmitField('Enviar')
