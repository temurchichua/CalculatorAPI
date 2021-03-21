from myapp import app
import math
from fractions import Fraction
from flask import request, jsonify


@app.route('/to_radians/<int:x>')
def toRadians(x):

    # format = request.args.get('format')
    integer = math.radians(x)

    return {"radian": integer, "degree": x}

if __name__ == '__main__':
    print(toRadians(7))