from sympy import FiniteSet

numbers = [i for i in range(1, 999)]

test_set = FiniteSet(*numbers)

print(test_set)
