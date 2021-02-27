class Cell:
    def __init__(self, number_of_cell):
        self.number_of_cell = number_of_cell

    def __add__(self, other):
        return self.number_of_cell + other.number_of_cell

    def __sub__(self, other):
        if self.number_of_cell - other.number_of_cell > 0:
            return self.number_of_cell - other.number_of_cell
        else:
            return other.number_of_cell - self.number_of_cell

    def __mul__(self, other):
        return self.number_of_cell * other.number_of_cell

    def __truediv__(self, other):
        if self.number_of_cell / other.number_of_cell > 0:
            return round(self.number_of_cell / other.number_of_cell)
        else:
            return round(other.number_of_cell / self.number_of_cell)

    @property
    def make_order(self):
        return ''.join([(self.number_of_cell//3)*'***\n', (self.number_of_cell%3)*'*'])


a = Cell(5)
b = Cell(8)
print(a+b)
print(a-b)
print(a/b)
print(a.make_order)
print(b.make_order)
