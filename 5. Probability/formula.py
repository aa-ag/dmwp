from sympy import FiniteSet, pi

def time_period(lenght):
    g = 9.8
    t = 2 * pi * (lenght/g) ** 0.5
    return t


if __name__ == "__main__":
    l = FiniteSet(15, 18, 21, 22.5, 25)
    for i in l:
        t = time_period(1/100)
        print('Lenght: {0} cm Time Period: {1:.3f} s'.format(float(i), float(t)))

