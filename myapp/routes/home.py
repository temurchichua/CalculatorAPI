from CalculatorAPI.myapp import app


@app.route("/")
def home():
    return "Welcome Screen"
