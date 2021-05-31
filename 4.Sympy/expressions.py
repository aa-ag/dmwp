from sympy.core.function import expand
from sympy.core.symbol import Symbol
from sympy import factor, pprint

x = Symbol('x')
y = Symbol('y')

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
pprint(expr)
'''
  3      2          2    3
x  + 3⋅x ⋅y + 3⋅x⋅y  + y 
'''
