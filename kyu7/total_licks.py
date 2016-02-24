def total_licks(env):
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
