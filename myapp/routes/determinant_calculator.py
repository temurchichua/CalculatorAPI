from myapp import app
from flask import request


@app.route('/calcdt', methods=['POST'])
def post_to_function():
    received_data = request.get_json()
    matrix = received_data['matrix']

    if type(matrix) is not list:
        return "Sent data needs to be a list of lists containing integers or floats", 400

    result = calculate_determinant(matrix)

    return str(result), 200


def calculate_determinant(matrix, check_matrix_validity = 1):
    matrix_size = len(matrix)
    operator = -1
    result = 0

    # Shevamowmot tu migebuli matricis ganzomilebebi sworia
    if check_matrix_validity == 1:
        matrix_is_square = all(len(row) == matrix_size for row in matrix)
        if matrix_is_square is False:
            return "მატრიცა უნდა შეიცავდეს სვეტების და მწკრივების ტოლ რაოდენობას"

    # Tu matrica aris organzomilebiani, pirdapir davabrunot pasuxi
    if matrix_size == 2:
        result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return result

    # Tu ar aris, mashin shevamcirot is ramodenime organzomilebian matricamde da davajamot isini
    for column in range(matrix_size):
        submatrix = matrix[1:]
        submatrix_size = len(submatrix)
        multiplier = matrix[0][column]

        for i in range(submatrix_size):
            submatrix[i] = submatrix[i][0:column] + submatrix[i][column + 1:]

        operator *= -1
        submatrix_determinant = calculate_determinant(submatrix, 0)  # Recursion!

        result += operator * multiplier * submatrix_determinant

    return result
