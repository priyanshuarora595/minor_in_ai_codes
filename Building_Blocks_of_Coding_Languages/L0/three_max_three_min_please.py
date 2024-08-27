def solve(N, arr):
    # Write code here
    arr = sorted(set(arr))
    if len(arr) <= 2:
        print("Not Possible")
        print("Not Possible")
    else:
        print(arr[0], arr[1], arr[2])
        print(arr[-3], arr[-2], arr[-1])
