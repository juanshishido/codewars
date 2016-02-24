def accum(s):
    """Given a string, `s`, duplicate each character based on its
    index position (plus one) and capitalize the first character
    in the sequence. Concatenate the resulting sequences, separating
    them with a `'-'`.

    Parameters
    ----------
    s = str
        input string

    Returns
    -------
    str
    """
    assert s.isalpha(), 'String can only include [a-zA-Z]'
    multiples = [i+1 for i in range(len(s))]
    z = zip(s, multiples)
    return '-'.join([(c[0]*c[1]).title() for c in z])
