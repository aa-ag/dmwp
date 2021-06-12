# find range / dispersion

def find_range(l):

    lowest = min(l)
    highest = max(l)
    rng = highest - lowest
    return lowest, highest, rng


if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 502, 600, 1000, 1200]
    lowest, highest, r = find_range(donations)
    print(
        'Lowest: {0}\nHihghest: {1}\nRange: {2}'.format(lowest, highest, r))
