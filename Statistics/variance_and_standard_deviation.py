############------------ GLOBAL VARIABLES ------------############
numbers = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]


############------------ FUNCTIONS ------------############
def calculate_mean(numbers):
    '''
     calculate mean of a list of integers
    '''
    numbers_sum = sum(numbers)
    list_lenght = len(numbers)
    return numbers_sum / list_lenght


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    pass
