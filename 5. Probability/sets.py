from sympy import FiniteSet

numbers = FiniteSet(1, 2, 3)

print(numbers.powerset())
# FiniteSet(FiniteSet(1), FiniteSet(1, 2), FiniteSet(1, 3), FiniteSet(1, 2, 3), FiniteSet(2), FiniteSet(2, 3), FiniteSet(3), EmptySet)
