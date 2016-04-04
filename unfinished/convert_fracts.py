from functools import reduce


def convert_fracts(lst):
    original_denominators = [f[1] for f in lst]
    common_denominator = reduce(lambda x, y: x*y, original_denominators)
    lcd = 1
    for d in range(max(original_denominators) + 1, common_denominator + 1):
        if all([d % x == 0 for x in original_denominators]):
            lcd = d
            break
    return [[x[0] * (lcd / x[1]), lcd] for x in lst]
