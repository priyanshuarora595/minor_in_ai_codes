def factors(n):
    # Complete code for this function
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)

    return set(sorted(factors))


def common_factors(a, b):
    # Complete code for this function
    factors_a = factors(a)
    factors_b = factors(b)
    return factors_a.intersection(factors_b)


def factors_upto(n):
    # Complete code for this function
    result = {}
    for i in range(1, n + 1):
        result[i] = factors(i)

    return result
