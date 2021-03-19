from myapp import app


def factorial(n):
    if n == 1:
        return n
    else:

        return n * factorial(n - 1)

@app.route('/factorial/<int:n>')
def factorial_handler(n):
    return {"result": factorial(n)}




