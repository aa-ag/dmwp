###--- IMPORTS ---###
from fractions import Fraction


###--- FUNCTIONS ---###
def create_a_fraction():
    f = Fraction(3, 4)
    print(type(f))  # <class 'fractions.Fraction'>
    print(f)  # 3/4


###--- DRIVER CODE ---###
if __name__ == "__main__":
    create_a_fraction()
