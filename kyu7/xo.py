def xo(s):
    """Check to see if a string has the same number of 'x's and 'o's.
    
    Parameters
    ----------
    s : str
        input string
    
    Returns
    -------
    bool
        True if the number of 'x's equals the number of 'o's
        or if there are no 'x's or 'o's
        False otherwise
    
    Examples
    --------
    >>> xo('ooxx')
    True
    >>> xo('xooxx')
    False
    >>> xo('ooxXm')
    True
    >>> xo('zpzpzpp')
    True
    >>> xo('zzoo')
    False
    """
    assert isinstance(s, str), '`s` must be type str'
    x = s.lower().count('x')
    o = s.lower().count('o')
    if x == 0 and o == 0:
        return True
    elif x == o:
        return True
    else:
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
