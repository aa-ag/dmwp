############------------ IMPORT(S) ------------############
from sympy import Limit, Symbol, S

############------------ CODE ------------############
n = Symbol('n')

# limit = Limit((1+1/n)**n, n, S.Infinity).doit()
# print(limit)
# # E

principal = Symbol('p')

rate = Symbol('r')

time = Symbol('t')

limit = Limit(principal * (1 + rate/n) ** (n * time), n, S.Infinity).doit()

print(limit)
# p*exp(r*t)