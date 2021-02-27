# Я не понял что делать с мнимым i и что это такое :(
class ComplexN:
    def __init__(self, a, b, i=1):
        self.a = a
        self.b = b
        self.i = i

    def __add__(self, other):
        return (self.a+other.a)+(self.b+other.b)*self.i

    def __mul__(self, other):
        return (self.a*other.a - self.b*other.b)+(self.a*other.b + self.b*other.a)


a = ComplexN(12, 3)
b = ComplexN(3, 5)
print(a+b)
print(a*b)
