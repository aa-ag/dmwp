from sympy.core.sympify import sympify

expression = input("Enter a mathematical expression:\n")
# 2*x + x**2

simpified = sympify(expression)
print(simpified)
# x**2 + 2*x

print(2*simpified)
# 2*x**2 + 4*x
