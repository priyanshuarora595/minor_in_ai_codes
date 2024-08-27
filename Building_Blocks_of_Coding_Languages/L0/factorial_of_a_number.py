def solve(N):
    # Write code here
    fact = 1
    for i in range(1, N + 1):
        fact *= i
    print(fact)
