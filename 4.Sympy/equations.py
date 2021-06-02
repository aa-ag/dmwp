from sympy.core import Symbol
from sympy.solvers.solvers import solve

x = Symbol('x')
expression = x - 5 - 7
print(solve(expression))
# [12]

expression = x + 4 - 6
print(solve(expression))
[2]
