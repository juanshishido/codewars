from itertools import combinations_with_replacement as cwr


def count_change(money, coins):
    vals = []
    for i in range(1, 25):
        vals.append([list(v) for v in cwr(coins, i)
                     if sum(v) == money])
    return len([v for v in vals if v != []])
