from sympy.core.symbol import Symbol

x = Symbol('x')
y = Symbol('y')

expression = x*x + x*y + x*y + y*y

# simple substitution
# evaluated_answer_with_values = expression.subs({x: 1, y: 2})
# print(evaluated_answer_with_values)
# 9

# one value in terms of another
evaluated_answer_with_values = expression.subs({x: 1-y})
print(evaluated_answer_with_values)
# y**2 + 2*y*(1 - y) + (1 - y)**2
