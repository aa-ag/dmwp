from sympy.core.symbol import Symbol
from sympy import factor

x = Symbol('x')
y = Symbol('y')

expression = (x ** 2) - (y ** 2)
print(factor(expression))
# (x - y)*(x + y)
