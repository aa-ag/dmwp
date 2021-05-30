######------ FUNCTIONS ------######
def calculate_mean(l):
    return sum(l) / len(l)


######------ TEST CASES ------######
def test_case_1():
    short_list = [1, 2, 3, 4, 5]
    return calculate_mean(short_list)


def test_case_2():
    longer_list = [i for i in range(100, 1100, 100)]
    return calculate_mean(longer_list)


######------ DRIVER CODE ------######
if __name__ == '__main__':
    # print(test_case_1())

    print(test_case_2())
