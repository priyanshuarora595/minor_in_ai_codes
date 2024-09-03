def solve(n, nums, x):
    # Write code here
    x = sorted(nums, key=lambda num: (abs(x - num), nums.index(num)))
    print(" ".join(map(str, x)))
