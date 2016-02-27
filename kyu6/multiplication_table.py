from itertools import product


def multiplication_table(row, col):
    r = range(1, row + 1)
    c = range(1, col + 1)
    return [[a*b for a in c] for b in r]
