############------------ FUNCTIONS ------------############
def measure_correlation(x, y):
    n = len(x)

    product = [(i * j) for i, j in zip(x, y)]

    print(product)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]
    measure_correlation(list_1, list_2)
