from myapp import app


@app.route('/sqr/<int:num>')
def square_number(num):
    return {f'Square number of {num}': num ** 2}

