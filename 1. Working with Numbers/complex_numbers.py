# a = 2 - 3j
# print(type(a))
# <class 'complex'>

# a = complex(2, 3)
# print(a)
# (2+3j)

# b = 3 + 3j
# print(a + b)
# (5+6j)

# print(a - b)
# (-1+0j)

# print(a * b)
# (-3+15j)

# print(a / b)
# (0.8333333333333334+0.16666666666666666j)

# z = 2 + 3j
# print(z.real)
# print(z.imag)
# print(z.conjugate())
# the magnitude of a complex number
# print((z.real ** 2 + z.imag ** 2) ** 0.5)  # 3.605551275463989
# or
# print(abs(z))  # 3.605551275463989
# print(abs(z) == (z.real ** 2 + z.imag ** 2) ** 0.5)  # True

############------------ cmath library ------------############
# https://docs.python.org/3/library/cmath.html
import cmath


print(cmath.phase(complex(-1.0, 0.0)))
# 3.141592653589793

print(cmath.pi)
# 3.141592653589793

print(cmath.inf)
# inf
