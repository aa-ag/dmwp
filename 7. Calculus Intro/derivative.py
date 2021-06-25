############------------ IMPORT(S) ------------############
from sympy import Symbol, Derivative

############------------ CODE ------------############
t = Symbol('t')

st = 5*t**2 + 2*t + 8

derivative = Derivative(st, t)

print(derivative.doit())
# 10*t + 2