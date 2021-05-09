###--- IMPORTS ---###
from fractions import Fraction


###--- FUNCTIONS ---###
def create_a_fraction():
    f = Fraction(3, 4)
    # print(type(f))  # <class 'fractions.Fraction'>
    print(f)  # 3/4
    print(f + 1 + 1.5)  # 3.25


###--- DRIVER CODE ---###
if __name__ == "__main__":
    create_a_fraction()
