class Matrix:
    def __init__(self, list_l):
        self.list_l = list_l

    def __str__(self):
        return '\n'.join(map(str, self.list_l))

    def __add__(self, other):
        empty = []
        for i in range(len(self.list_l)):
            empty.append([])
            for d in range(len(self.list_l[0])):
                empty[i].append(self.list_l[i][d] + other.list_l[i][d])
        return '\n'.join(map(str, empty))


a = [[1, 2, 3, 45], [5, 78, 48, 4]]
b = [[4, 56, 7, 8], [6, 7, 9, 100]]
print(Matrix(b), '\n')
print(Matrix(a), '\n')
print(Matrix(a)+Matrix(b))
