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

'''
  Length(cm)   Gravity(m/s^2) Time Period(s) 
     15.0           9.78           0.201     
     18.0           9.78           0.201     
     15.0            9.8           0.201     
     21.0           9.78           0.201     
     18.0            9.8           0.201     
     15.0           9.83           0.200     
     22.5           9.78           0.201     
     21.0            9.8           0.201     
     18.0           9.83           0.200     
     25.0           9.78           0.201     
     22.5            9.8           0.201     
     21.0           9.83           0.200     
     25.0            9.8           0.201     
     22.5           9.83           0.200     
     25.0           9.83           0.200 
'''