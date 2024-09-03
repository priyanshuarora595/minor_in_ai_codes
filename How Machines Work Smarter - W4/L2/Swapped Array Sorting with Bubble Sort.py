def solve(nums):
    # Write code here
    sorted_arr = modified_bubble_sort(nums)
    print(" ".join(map(str, sorted_arr)))


def modified_bubble_sort(arr):
    n = len(arr)

    # Perform a single pass of Bubble Sort to fix the swapped pair
    swapped = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            # Swap the out-of-order elements
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
            break  # Exit after one swap, since only one pair is swapped

    # If a swap was made, check if the array is now sorted
    if swapped:
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                # If still not sorted, call the function recursively
                return modified_bubble_sort(arr)

    return arr
