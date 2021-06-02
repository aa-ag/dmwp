from sympy.core.sympify import sympify, SympifyError

try:
    expression = input("Enter a mathematical expression:\n")
    # x**2 + 3*3 + x**3 + 2x

    simpified = sympify(expression)
    print(simpified)
    print(2*simpified)

except SympifyError:
    print("Invalid Input")
    # Invalid Input
