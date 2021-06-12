from sympy.core.symbol import Symbol, symbols

x, y, z = symbols('x,y,z')
s = x*y + x*y
print(s)
# 2*x*y
