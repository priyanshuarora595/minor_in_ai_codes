def concatenate_array(n, nums):
    if n != 0:
        ans = []
        ans += 2 * nums
        return ans


n = int(input())
if n != 0:
    input_str = input()
    input_list = list(map(int, input_str.split()))
    print(*(concatenate_array(n, input_list)))
else:
    print()
