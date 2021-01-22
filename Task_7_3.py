class Cell:
    def __init__(self, number_of_cells):
        self.number = int(number_of_cells)

    def __add__(self, other_cell):
        return self.number + other_cell.number

    def __sub__(self, other_cell):
        if (self.number - other_cell.number) > 0:
            return self.number - other_cell.number
        else:
            return 'Вычитание невозможно'

    def __mul__(self, other_cell):
        return self.number * other_cell.number

    def __truediv__(self, other_cell):
        return self.number // other_cell.number

    def make_order(self, cells_in_row):
        temp = self.number
        new_str = ''
        cell_str = ''
        while temp > cells_in_row:
            new_str = new_str.ljust(cells_in_row, '*')
            new_str += '\n'
            temp -= cells_in_row
            cell_str += new_str
            new_str = ''
        cell_str += new_str.ljust(temp, '*')
        return cell_str.ljust(temp, '*')


cell_1 = Cell(5)
cell_2 = Cell(10)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_2 / cell_1)
# print(cell_1.make_order(4))
print(cell_2.make_order(3))
