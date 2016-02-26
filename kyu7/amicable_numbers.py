def amicable_numbers(n1, n2):
    n1_divisors = [n for n in range(1, n1) if n1 % n == 0]
    n2_divisors = [n for n in range(1, n2) if n2 % n == 0]
    return sum(n1_divisors) == n2 and sum(n2_divisors) == n1
