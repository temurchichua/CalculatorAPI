from myapp import app

@app.route('/factorial/<int:n>')
def factorial(n):

    if n == 1:
        return n
    else:
        return n*factorial(n-1)
