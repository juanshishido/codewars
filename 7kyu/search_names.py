def search_names(logins):
    """
    Examples
    --------
    >>> search_names([['foo', 'foo@foo.com'], ['bar_', 'bar@bar.com']])
    [['bar_', 'bar@bar.com']]
    """
    assert isinstance(logins, list), 'Must be type list'
    return list(filter((lambda x: x[0][-1] == '_'), logins))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
