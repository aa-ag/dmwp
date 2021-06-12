from sympy import FiniteSet

numbers = FiniteSet(1, 2, 3)
more_numbers = FiniteSet(3, 4, 5)

print(numbers.intersection(more_numbers))
# FiniteSet(3)
