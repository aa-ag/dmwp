############------------ IMPORT(S) ------------############
from sympy import Limit, Symbol, S

############------------ CODE ------------############
n = Symbol('n')

limit = Limit((1+1/n)**n, n, S.Infinity).doit()
print(limit)
# E