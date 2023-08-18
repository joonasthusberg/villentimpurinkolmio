from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired
import math

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class DimensionForm(FlaskForm):
    dimension_a = FloatField('Ulottuvuus a', validators=[InputRequired()])
    submit = SubmitField('Laske')

@app.route('/', methods=['GET', 'POST'])
def calculate_dimension():
    form = DimensionForm()

    if form.validate_on_submit():
        dimension_a = form.dimension_a.data
        dimension_b = (4 / 3) * dimension_a
        dimension_c = (5 / 3) * dimension_a

        result_text = f"Ulottuvuus 'b': {dimension_b:.2f}\nUlottuvuus 'c': {dimension_c:.2f}"

        return render_template('index.html', form=form, result_text=result_text)

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
