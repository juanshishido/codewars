def get_sum(a, b):
    """
    Examples
    --------
    >>> get_sum(1, 0)
    1
    >>> get_sum(1, 2)
    3
    >>> get_sum(0, 1)
    1
    >>> get_sum(1, 1)
    1
    >>> get_sum(-1, 0)
    -1
    >>> get_sum(-1, 2)
    2
    """
    assert isinstance(a, int) and isinstance(b, int), 'Must be type int'
    return sum(range(min(a, b), max(a, b) + 1))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
