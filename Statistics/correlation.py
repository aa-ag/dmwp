############------------ FUNCTIONS ------------############
def measure_correlation(x, y):
    n = len(x)

    product_sum = sum([(i * j) for i, j in zip(x, y)])

    squared_x_sum = sum(x) ** 2
    squared_y_sum = sum(y) ** 2

    x_square_sum = sum([(xi ** 2) for xi in x])
    y_square_sum = sum([(yi ** 2) for yi in y])

    numerator = (n * product_sum) - (squared_x_sum * squared_y_sum)

    denominator_x_half = n * x_square_sum - squared_x_sum
    denominator_y_half = n * y_square_sum - squared_y_sum
    denominator = (denominator_x_half * denominator_y_half) ** 0.5

    correlation = numerator / denominator
    return correlation


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]
    print(measure_correlation(list_1, list_2))
