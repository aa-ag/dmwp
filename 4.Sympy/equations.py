from math import exp
from sympy.core import Symbol
from sympy.solvers.solvers import solve

x = Symbol('x')
expression = x**2 + x + 1

print(solve(expression, dict=True))
# [{x: -1/2 - sqrt(3)*I/2}, {x: -1/2 + sqrt(3)*I/2}]
