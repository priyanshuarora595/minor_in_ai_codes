def string_score(s):
    ans = 0
    for i in range(len(s) - 1):
        ans += abs(ord(s[i]) - ord(s[i + 1]))
    return ans
