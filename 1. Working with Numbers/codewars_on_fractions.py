from fractions import Fraction


def add_fracs(*args):
    if not args:
        return ''
    s = sum([Fraction(arg) for arg in args])

    if s.denominator == 1:
        return str(s.numerator)
    return f"{s.numerator}/{s.denominator}"


add_fracs()  # ''
add_fracs('1/2')  # '1/2'
add_fracs('1/2', '1/4')  # '3/4'
add_fracs('1/2', '3/4')  # '5/4'
add_fracs('2/4', '6/4', '4/4')  # '3'
add_fracs('2/3', '1/3', '4/6')  # '5/3'
add_fracs('2/3', '1/4', '5/6')  # '7/4'
add_fracs('-2/3', '5/3', '-4/6')  # '1/3'
add_fracs('-7/3', '-1/3', '-2/3')  # '-10/3'
add_fracs('1/4', '5/4', '-1/2', '-1/1')  # '0'
