from myapp import app
from flask import request


def mean(*args):
    try:
        sum1 = sum(args)
    except TypeError:
        return "Argument must be an integer or a float"

    n = len(args)
    result = sum1/n
    return result


@app.route('/mean', methods=['POST'])
def post():
    nums = request.get_json()
    return mean(nums)
