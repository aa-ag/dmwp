from sympy import FiniteSet

numbers = FiniteSet(1, 2, 3)
more_numbers = FiniteSet(4, 5, 6)

print(numbers.union(more_numbers))
# FiniteSet(1, 2, 3, 4, 5, 6)
