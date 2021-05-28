############------------ FUNCTIONS ------------############
def measure_correlation(x, y):
    n = len(x)

    prod = []

    for xi, yi in zip(x, y):
        prod.append(xi*yi)

    sum_prod_x_y = sum(prod)

    sum_x = sum(x)
    sum_y = sum(y)

    squared_sum_x = sum_x ** 2
    squared_sum_y = sum_y ** 2

    x_square = []

    for xi in x:
        x_square.append(xi ** 2)

    x_square_sum = sum(x_square)

    y_square = []

    for yi in y:
        y_square.append(yi ** 2)

    y_square_sum = sum(y_square)

    numerator = n * sum_prod_x_y - sum_x * sum_y

    denominator_term1 = n * x_square_sum - squared_sum_x
    denominator_term2 = n * y_square_sum - squared_sum_y
    denominator = (denominator_term1 * denominator_term2) ** 0.5

    correlation = numerator/denominator
    return correlation


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]
    print(measure_correlation(list_1, list_2))
