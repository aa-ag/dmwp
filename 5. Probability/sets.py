from sympy import FiniteSet

numbers = FiniteSet(1, 2, 3, 4, 5, 6)

subset_of_numbers = FiniteSet(3, 2, 1)

print(subset_of_numbers.is_subset(numbers))
# True
