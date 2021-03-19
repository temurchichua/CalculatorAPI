from myapp import app
from flask import request, jsonify

@app.route('/mean', methods=['POST'])
def post_mean():
    data = request.get_json()
    nums = data["numbers"]
    try:
        sum1 = sum(nums)
    except TypeError:
        return "Argument must be an integer or a float", 400
    n = len(nums)
    result = sum1/n
    return jsonify(result), 200
