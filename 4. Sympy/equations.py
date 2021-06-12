from math import exp
from sympy.core import Symbol
from sympy.solvers.solvers import solve

x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
expression = a*x*x + b*x + c

print(solve(expression, x, dict=True))
# [{x: (-b + sqrt(-4*a*c + b**2))/(2*a)}, {x: -(b + sqrt(-4*a*c + b**2))/(2*a)}]
