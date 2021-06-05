from math import exp
from sympy.core import Symbol
from sympy.solvers.solvers import solve

x = Symbol('x')
expression = x**2 + 5*x + 4
print(solve(expression))
# [-4, -1]
