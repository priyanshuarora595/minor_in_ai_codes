def biggest_good_digit(num):
    ans = -1
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            if int(num[i]) > ans:
                ans = int(num[i])
    return ans
