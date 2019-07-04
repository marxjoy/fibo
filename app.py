from flask import Flask, render_template, request, url_for
from wtforms import Form, IntegerField, validators
from fibo import fibo


app = Flask(__name__)

class FiboForm(Form):
    fibo_text_field = IntegerField('Który element ciągu Fibonacciego obliczyć?', [validators.Required('Podaj liczbę całkowitą'),validators.NumberRange(0, 35, 'Podaj liczbę z przedziału 0-35')], )

    
@app.route('/')
def index():
    form = FiboForm(request.form)
    return render_template('form.html', form=form)

@app.route('/result', methods=['POST'])
def result():
    form = FiboForm(request.form)
    if request.method == 'POST' and form.validate():
        n = request.form['fibo_text_field']
        result = fibo(int(n))
        return render_template('result.html', n=n, result=result)
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=False)