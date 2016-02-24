def head(arr):
    """
    Examples
    --------
    >>> head([1, 2, 3, 4, 5])
    1
    """
    return arr[0]

def tail(arr):
    """
    Examples
    --------
    >>> tail([1, 2, 3, 4, 5])
    [2, 3, 4, 5]
    >>> tail([1])
    []
    """
    return arr[1:]

def init(arr):
    """
    Examples
    --------
    >>> init([1, 2, 3, 4, 5])
    [1, 2, 3, 4]
    """
    return arr[:-1]

def last(arr):
    """
    Examples
    --------
    >>> last([1, 2, 3, 4, 5])
    5
    """
    return arr[-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
