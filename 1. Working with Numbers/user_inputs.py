from fractions import Fraction

try:
    a = Fraction(input("Enter a fraction: "))
except ZeroDivisionError:
    print("Invalid fraction")
