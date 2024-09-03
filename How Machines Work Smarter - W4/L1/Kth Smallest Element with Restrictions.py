def solve(n, nums, k):
    for i in range(k):
        elem = min(nums[i:])
        nums.remove(elem)
        nums.insert(i, elem)
    print(nums[k - 1])
