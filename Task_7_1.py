def function_list(list_matrix, number_of_row, number_of_coloumn):
    return (list_matrix[number_of_row])[number_of_coloumn]


class Matrix:
    def __init__(self, rows_and_columns):
        self.matrix = rows_and_columns

    def __str__(self):
        self.temp_str = ''
        for el in self.matrix:
            for element in el:
                self.temp_str += str(element)
                self.temp_str += ' '
            self.temp_str += '\n'
        return self.temp_str

    def return_list(self):
        return self.matrix

    def __add__(self, matrix_a):
        i = 0
        matrix_1 = self.matrix
        matrix_2 = matrix_a.matrix
        if len(matrix_1) != len(matrix_2):
            return 'Такие матрицы складывать нельзя'
        result = []
        while i < len(matrix_1):
            j = 0
            new_list = []
            while j < len(matrix_1[0]):
                new_list.append(function_list(matrix_1, i, j) + function_list(matrix_2, i, j))
                j += 1
            i += 1
            result.append(new_list)

        return Matrix(result).__str__()


matrix = Matrix([[3, 2, 1], [3, 2, 1]])
matrix_plus = Matrix([[3, 2, 3], [3, 2, 3]])
print(matrix + matrix_plus)
matrix_plus = matrix_plus.__str__()
print(matrix_plus)
matrix = matrix.__str__()
