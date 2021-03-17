from myapp import app


@app.route("/")
def home():
    return "Welcome Screen"
