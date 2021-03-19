from myapp import app


@app.route('/pythagoras/<int:a>&<int:b>')
def pythagoras(a, b):
    return {f'tu 1 kateti = {a} da meore = {b}, mashin hipotenuza iqneba': ((a*a)+(b * b))**(1 / 2)}
