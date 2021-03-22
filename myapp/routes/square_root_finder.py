from myapp import app


@app.route('/square_root/<int:number>')
def square_root(number):
    return {f'Square root of the number is {number}': number ** 0.5}
