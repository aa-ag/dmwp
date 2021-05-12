class Complex:
    def __init__(self, re, im):
        self.real = re
        self.imaginary = im

    def __add__(self, other):
        return Complex(self.real+other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imaginary*other.imaginary,
                       self.real*other.imaginary + other.real*self.imaginary)


# TESTS & DRIVER CODE
print(Complex(1, 0).real)  # 1
print(Complex(2, 0).real)  # 2
print(Complex(0, 0).real)  # 0
print(Complex(0, 1).real)  # 0

print(Complex(1, 0).imaginary)  # 0
print(Complex(2, 0).imaginary)  # 0
print(Complex(0, 0).imaginary)  # 0
print(Complex(0, 1).imaginary)  # 1

# add = Complex(1, 0) + Complex(0, 1)
# print([add.real, add.imaginary])  # [1, 1]

# m = Complex(2, 2) * Complex(3, 3)
# print([m.real, m.imaginary])  # [0, 12]
