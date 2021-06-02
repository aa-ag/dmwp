############------------ IMPORTS ------------############
from sympy.core import expand, sympify, SympifyError


############------------ FUNCTIONS ------------############
def product(expression_1, expression_2):
    p = expand(expression_1 * expression_2)
    print(p)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    expression_1 = input("Enter first expression: \n")
    expression_2 = input("Enter second expression: \n")
    try:
        x1 = sympify(expression_1)
        x2 = sympify(expression_2)
        print(product(expression_1, expression_2))
    except SympifyError:
        print("Invalid Input")
