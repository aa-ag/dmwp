from sympy.core.symbol import Symbol

x = Symbol('x')
y = Symbol('y')

expression = x*x + x*y + x*y + y*y

evaluated_answer_with_values = expression.subs({x: 1, y: 2})
print(evaluated_answer_with_values)
# 9
