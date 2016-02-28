def iq(numbers):
    numbers = [int(n) % 2 for n in numbers.split()]
    if sum(numbers) == 1:
        return numbers.index(1) + 1
    else:
        return numbers.index(0) + 1
