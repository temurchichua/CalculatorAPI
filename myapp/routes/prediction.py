from myapp import app


@app.route('/lnreg/<int:num>', methods=['POST'])
def post_regression(num):

    def linear_regression(data_x, data_y):
        min_len = min(len(data_y), len(data_x))
        avg_x = sum(data_x) / len(data_x)
        avg_y = sum(data_y) / len(data_y)
        x1 = 0
        x2 = 0

        for i in range(min_len):
            xminxavg = data_x[i] - avg_x
            x1 += xminxavg * (data_y[i] - avg_y)
            x2 += xminxavg * xminxavg

        b = x1 / x2
        a = avg_y - b * avg_x
        regr = a + b * float(num)
        return regr

    try:
        data = request.get_json()
        data1 = data['data_x']
        data2 = data['data_y']
    except Exception as error:
        return {error: "Try the following format: {'data_x: [list of int/floats]}, {data_y: [list of int/floats]}"}

    result = {'message': f'Data_x: {data1}, Data_y: {data2}, Prediction: {linear_regression(data1, data2)}'}
    return result
