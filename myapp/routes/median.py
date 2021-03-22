from myapp import app
from flask import request

def median(data):
    n = len(data)
    data.sort()

    if n % 2 == 0:
        median1 = data[n // 2]
        median2 = data[n // 2 - 1]
        med = (median1 + median2) / 2
    else:
        med = data[n // 2]
    return f"Median for your list is: {str(med)}"

@app.route('/median/', methods=['POST'])
def medianer():
    num_list = request.get_json().get('numbers')
    print(num_list)
    return {"result": median(num_list)}