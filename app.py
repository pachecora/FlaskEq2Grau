from flask import Flask, render_template, session, url_for, redirect, request
from model import Formulario
from equacao import equacao2grau

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='QUALQUERcOISAsERVE')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Formulario()
    if form.validate_on_submit():
        session['a'] = form.a.data
        session['b'] = form.b.data
        session['c'] = form.c.data
        return redirect(url_for('index'))

    raizes = equacao2grau(session.get('a'), session.get('b'), session.get('c'))
    return render_template('index.html',
                           form=form,
                           a=session.get('a'),
                           b=session.get('b'),
                           c=session.get('c'),
                           raiz1=raizes[0],
                           raiz2=raizes[1],)


if __name__ == '__main__':
    app.run(debug=True)
