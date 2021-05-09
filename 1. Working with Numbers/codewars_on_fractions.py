'''
 https://www.codewars.com/kata/5816f2580e80c5e075000a4f/train/python
'''

######------ IMPORTS ------######
from fractions import Fraction


######------ FUNCTIONS ------######
def add_fracs(*args):
    return str(sum(Fraction(a) for a in args)) if args else ''


######------ TESTS ------######
print(add_fracs())  # ''
print(add_fracs('1/2'))  # '1/2'
print(add_fracs('1/2', '1/4'))  # '3/4'
print(add_fracs('1/2', '3/4'))  # '5/4'
print(add_fracs('2/4', '6/4', '4/4'))  # '3'
print(add_fracs('2/3', '1/3', '4/6'))  # '5/3'
print(add_fracs('2/3', '1/4', '5/6'))  # '7/4'
print(add_fracs('-2/3', '5/3', '-4/6'))  # '1/3'
print(add_fracs('-7/3', '-1/3', '-2/3'))  # '-10/3'
print(add_fracs('1/4', '5/4', '-1/2', '-1/1'))  # '0'
