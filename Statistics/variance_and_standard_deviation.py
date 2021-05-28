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


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    numbers = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    variance = find_variance(numbers)
    print(f"The variance of this list of numbers is {round(variance, 2)}")

    standard_deviation = variance ** 0.5
    print(
        f"The standard deviation of the list is {round(standard_deviation, 2)}")
