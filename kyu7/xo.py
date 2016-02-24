def xo(s):
    assert isinstance(s, str), '`s` must be type str'
    x = s.lower().count('x')
    o = s.lower().count('o')
    if x == 0 and o == 0:
        return True
    elif x == o:
        return True
    else:
        return False
