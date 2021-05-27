######------ FUNCTIONS ------######
def calculate_mean(l):
    return sum(l) / len(l)


######------ DRIVER CODE ------######
def test_case_1():
    short_list = [1, 2, 3, 4, 5]
    return calculate_mean(short_list)


######------ DRIVER CODE ------######
if __name__ == '__main__':
    print(test_case_1())
