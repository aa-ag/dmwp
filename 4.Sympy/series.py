from sympy.core.symbol import Symbol
from sympy import pprint, init_printing


def print_series(n):
    init_printing(order="rev-lex")

    x = Symbol('x')

    series = x

    for i in range(2, n+1):
        series = series + (x**i)/i
    pprint(series)


if __name__ == '__main__':
    n = input("Enter the number of terms you want in the series:\n")
    print_series(int(n))

    '''
            2    3    4    5
        x    x    x    x 
    x + ── + ── + ── + ──
        2    3    4    5 
    '''
