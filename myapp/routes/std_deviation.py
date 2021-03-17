from myapp import app


@app.route('/stddev/<string:numbers>', methods=['GET'])
def get_stddev(numbers):

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

    pop_data = numbers.split(',')
    pop_data_int = []
    for n in pop_data:
        pop_data_int.append(int(n))
    json_to_return = {'message': f'Received data: {pop_data_int} Standard Deviation: {std_deviation(pop_data_int)}'}
    return json_to_return, 200
