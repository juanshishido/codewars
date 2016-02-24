def total_licks(env):
    """
    Examples
    --------
    >>> total_licks({"freezing temps": 10, "clear skies": -2})
    'It took 260 licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was freezing temps.'
    >>> total_licks({"happiness": -5, "clear skies": -2})
    'It took 245 licks to get to the tootsie roll center of a tootsie pop.'
    >>> total_licks({})
    'It took 252 licks to get to the tootsie roll center of a tootsie pop.'
    >>> total_licks({"dragons": 100, "evil wizards": 110, "trolls": 50})
    'It took 512 licks to get to the tootsie roll center of a tootsie pop. The toughest challenge was evil wizards.'
    >>> total_licks({"white magic": -250})
    'It took 2 licks to get to the tootsie roll center of a tootsie pop.'
    """
    baseline = 252
    for licks in env.values():
        baseline += licks
    s_licks = 'It took %s licks to get to the tootsie roll center of a tootsie pop.' % baseline
    if len(env) > 0:
        max_licks = max(env.values())
        if max_licks > 0:
            challenging_condition = [k for k, v in env.items() if v == max_licks]
            s_challenge = 'The toughest challenge was %s.' % challenging_condition[0]
            return s_licks + ' ' + s_challenge
    return s_licks


if __name__ == '__main__':
    import doctest
    doctest.testmod()
