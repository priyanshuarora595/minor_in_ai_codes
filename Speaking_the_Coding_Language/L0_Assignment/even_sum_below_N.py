def solve(num):
    """You are not supposed to take input.
    Input value is already given to you
    as num. You just need to use this value
    to write down the program.
    """
    # Write code here
    ans = 0
    for i in range(2, num + 1, 2):
        ans += i

    print(ans)
