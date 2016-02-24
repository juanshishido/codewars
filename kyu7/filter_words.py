from re import sub

def filter_words(phrase):
    """
    Examples
    --------
    >>> filter_words("You're Bad! timmy!")
    "You're awesome! timmy!"
    >>> filter_words("You're MEAN! timmy!")
    "You're awesome! timmy!"
    """
    return sub(r'(?i)(bad|mean|ugly|horrible|hideous)', 'awesome', phrase)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
