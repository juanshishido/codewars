def longest_slide_down(pyramid):
    pyramid.reverse()
    for i in range(1, len(pyramid)):
        sums = []
        for j in range(len(pyramid[i])):
            sums.append(max(pyramid[i][j] + pyramid[i-1][j],
                            pyramid[i][j] + pyramid[i-1][j+1]))
        pyramid[i] = sums
    return pyramid[-1][0]
