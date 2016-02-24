def get_sum(a, b):
    assert isinstance(a, int) and isinstance(b, int), 'Must be type int'
    return sum(range(min(a, b), max(a, b) + 1))
