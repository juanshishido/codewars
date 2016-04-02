def is_merge(s, part1, part2):
    all_chars = len(s) == len(part1) + len(part2)
    if not all_chars:
        return False
    d = {}
    for i, c in enumerate(s):
        d[c] = i
    indices1, indices2 = [d[c] for c in part1], [d[c] for c in part2]
    part1_good = indices1 == sorted(indices1)
    part2_good = indices2 == sorted(indices2)
    return part1_good and part2_good
