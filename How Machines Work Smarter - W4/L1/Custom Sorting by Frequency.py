def solve(n, nums):
    x = sorted(nums, key=lambda num: (nums.count(num), nums.index(num)))
    print(" ".join(map(str, x)))
