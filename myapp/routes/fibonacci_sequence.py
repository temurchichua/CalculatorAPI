from myapp import app
from flask import jsonify


@app.route('/sequence/<int:max_num>')
def Fibonacci(max_num):
    firstNum = 0
    secondNum = 1
    sequence = []
    print(secondNum)
    thirdNum = firstNum + secondNum
    print(thirdNum)
    while (thirdNum + secondNum) < max_num:
        firstNum = secondNum
        secondNum = thirdNum
        thirdNum = firstNum + secondNum
        sequence.append(thirdNum)
    return jsonify(sequence), 201

