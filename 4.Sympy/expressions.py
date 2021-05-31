from sympy.core.function import expand
from sympy.core.symbol import Symbol
from sympy import factor

x = Symbol('x')
y = Symbol('y')

expression = (x ** 2) - (y ** 2)

factors = factor(expression)
print(expand(factors))
# x**2 - y**2
