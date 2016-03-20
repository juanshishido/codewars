from itertools import permutations as prm


def permutations(s):
    return list(set([''.join(p) for p in prm(s, len(s))]))
