############------------ FUNCTIONS ------------############
def calculate_mean(numbers):
    '''
     calculate mean of a list of integers
    '''
    numbers_sum = sum(numbers)
    list_lenght = len(numbers)
    return numbers_sum / list_lenght


def find_differences(numbers):
    '''
     calculate distance from each number to the mean
    '''
    mean = calculate_mean(numbers)
    differences = [(number - mean) for number in numbers]
    return differences


def find_variance(numbers):
    differences = find_differences(numbers)

    squared_differences = [(j ** 2) for j in differences]

    total_squared_differences = sum(squared_differences)

    variance = total_squared_differences / len(numbers)

    return variance

############------------ TESTS ------------############


def test_case_1():
    '''
     testing list with high variance, 
     and high standard deviation
    '''
    numbers = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = find_variance(numbers)
    print(f"The variance of this list of numbers is {round(variance, 2)}")
    # The variance of this list of numbers is 141047.35

    standard_deviation = variance ** 0.5
    print(
        f"The standard deviation of the list is {round(standard_deviation, 2)}")
    # The standard deviation of the list is 375.56


def test_case_2():
    '''
     testing list with low variance, 
     and low standard deviation
    '''
    numbers = [382, 389, 377, 397, 396, 368, 369, 392, 398, 367, 396]
    variance = find_variance(numbers)
    print(f"The variance of this list of numbers is {round(variance, 2)}")
    # The variance of this list of numbers is 141.87

    standard_deviation = variance ** 0.5
    print(
        f"The standard deviation of the list is {round(standard_deviation, 2)}")
    # The standard deviation of the list is 11.91


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    test_case_1()
    test_case_2()
