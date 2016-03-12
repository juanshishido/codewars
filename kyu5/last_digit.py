def last_digit(n1, n2):
    if n2 == 0:
        return 1
    lasts = []
    for i in range(1, 10):
        last = int(str(n1 ** i)[-1])
        if last in lasts:
            break
        lasts.append(last)
    position = n2 % len(lasts) - 1
    return lasts[position]
