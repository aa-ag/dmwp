###--- IMPORTS ---###
from fractions import Fraction
# https://docs.python.org/3/library/fractions.html


###--- FUNCTIONS ---###
def create_a_fraction():
    # Fraction object has `numberator` and `denominator`
    # always in this order ^
    f = Fraction(3, 4)
    # print(type(f))  # <class 'fractions.Fraction'>
    print(f)  # 3/4
    print(f + 1 + 1.5)  # 3.25

    print(Fraction(3, 4) + 1 + Fraction(1/4))


###--- DRIVER CODE ---###
if __name__ == "__main__":
    create_a_fraction()
