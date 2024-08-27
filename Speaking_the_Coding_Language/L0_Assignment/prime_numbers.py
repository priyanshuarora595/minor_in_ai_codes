def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def solve(l, r):
    """You are not supposed to take input.
    Input values are already given to you
    as l & r. You just need to use these values
    to write down the program.
    """
    # Write code here
    for i in range(l, r + 1):
        if is_prime(i):
            print(i, end=" ")
