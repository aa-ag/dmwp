######------ FUNCTIONS ------######
def calculate_median(l):
    length = len(l)
    l.sort()
    if length % 2 == 0:
        even_m1 = int(length / 2) - 1
        even_m2 = int((length / 2) + 1) - 1

        return (l[even_m1] + l[even_m2]) / 2
    else:
        odd_m = int((length + 1) / 2) - 1
        return l[odd_m]


######------ TEST CASES ------######
def test_case_1():
    return calculate_median([100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200])


######------ DRIVER CODE ------######
if __name__ == '__main__':
    print(test_case_1())
