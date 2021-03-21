from myapp import app
import math
from fractions import Fraction


@app.route('/to_radians/<int:x>')
def toRadians(x):
    integer = math.radians(x)
    return f"{Fraction.from_float(integer).limit_denominator(10)} იგივე რაც {integer} რადიანი"

if __name__ == '__main__':
    print(toRadians(7))