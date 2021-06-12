############------------ FUNCTIONS ------------############
import pandas as pd


############------------ FUNCTIONS ------------############
def measure_correlation(x, y):
    x_series = pd.Series(x)
    y_series = pd.Series(y)
    return x_series.corr(y_series)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]
    print(measure_correlation(list_1, list_2))
