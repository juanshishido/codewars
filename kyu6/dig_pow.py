def dig_pow(n, p):
    exp_digits = [int(d) ** (e + p) for e, d in enumerate(str(n))]
    k, remainder = divmod(sum(exp_digits), n)
    if remainder:
        k = -1
    return k
