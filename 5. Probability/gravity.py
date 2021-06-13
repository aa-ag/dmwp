from sympy import FiniteSet, pi

def time_period(length, g):
    return 2 * pi * (length/g) ** 0.5


if __name__ == "__main__":
    l = FiniteSet(15, 18, 21, 22.5, 25)
    g_values = FiniteSet(9.8, 9.78, 9.83)
    print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)', 'Gravity(m/s^2)', 'Time Period(s)'))
    for i in l * g_values:
        le = i[0]
        g = i[1]
        t = time_period(1/100, g)
        print('{0:^15}{1:^15}{2:^15.3f}'.format(float(le), float(g), float(t)))