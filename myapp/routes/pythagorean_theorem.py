from myapp import app
from flask import request


@app.route('/pythagorean_theorem/<string:unknown_side>', methods=['POST'])
def pythagorean_theorem(unknown_side):
    data = request.json
    a = data["a"]
    b = data["b"]
    try:
        a - b
    except Exception as error_message:
        return {"ErrorMessage": f"{error_message}"}
    else:
        if a <= 0 or b <= 0:
            return {"message": "None of the triangle's side's length can be equal to 0, or smaller than 0!"}
        else:
            if unknown_side.lower() == "hypotenuse":
                c2 = (a ** 2) + (b ** 2)
                c = c2 ** (1 / 2)
                return {"message": f"Unknown hypotenuse's length is: {c}"}

            elif unknown_side.lower() == "leg":
                if a > b:
                    c2 = (a ** 2) - (b ** 2)
                    c = c2 ** (1 / 2)
                    return {"message": f"Unknown leg's length is: {c}"}

                elif a < b:
                    c2 = (b ** 2) - (a ** 2)
                    c = c2 ** (1 / 2)
                    return {"message": f"Unknown leg's length is: {c}"}

                elif a == b:
                    return {"ErrorMessage": "Leg and hypotenuse can not be the same length!"}

                else:
                    return {"ErrorMessage": "Something went wrong!"}
            else:
                return {"message": "Please insert unknown side as: Hypotenuse or Leg!"}
