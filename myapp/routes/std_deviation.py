from myapp import app
from flask import request


@app.route('/stddev', methods=['POST'])
def post_stddev():

    def std_deviation(population_list):
        """calculates population standard deviation by taking population data as a list"""

        # checking if the argument (population_list and its data) is valid
        if type(population_list) != list and type(population_list) != tuple:
            return "Error: the received argument should be of 'list' or 'float' type"
        for n in population_list:
            if type(n) != int and type(n) != float:
                return "Error: the received data inside list should be of 'integer' or 'float' type"

        # calculating mean
        sum_1 = 0
        for n in population_list:
            sum_1 += n
        mean = sum_1 / len(population_list)

        # subtracting mean from each number and squaring the result
        squared_differences = []
        for n in population_list:
            squared_differences.append((n - mean) ** 2)

        # calculating mean of squared_differences and taking the square root of the result
        sum_2 = 0
        for n in squared_differences:
            sum_2 += n
        new_mean = sum_2 / len(population_list)
        standard_deviation = new_mean ** 0.5
        return standard_deviation

    # receive data and calculate st.d.
    try:
        data = request.get_json()
        pop_data = data['population']
    except Exception as error_message:
        return {error_message: "no JSON or invalid JSON received. Valid format: {'population: [list of integers or floats]}"}, 400
    json_to_return = {'message': f'Received data: {pop_data} Standard Deviation: {std_deviation(pop_data)}'}
    return json_to_return, 200
