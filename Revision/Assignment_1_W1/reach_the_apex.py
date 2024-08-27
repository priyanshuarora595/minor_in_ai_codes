def stairs(x):
    if x == 0 or x == 1:
        return 1

    prev1 = 1
    prev2 = 1

    for i in range(2, x + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1
