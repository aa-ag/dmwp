from sympy.core.function import expand
from sympy.core.symbol import Symbol
from sympy import factor

x = Symbol('x')
y = Symbol('y')

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3

factors = factor(expr)
print(factors)
# (x + y)**3
