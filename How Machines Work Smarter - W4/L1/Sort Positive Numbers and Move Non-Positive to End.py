def solve(n, nums):
    non_positives = [i for i in nums if i <= 0]
    positives = [i for i in nums if i > 0]
    positives.sort()
    print(" ".join(map(str, positives + non_positives)))
