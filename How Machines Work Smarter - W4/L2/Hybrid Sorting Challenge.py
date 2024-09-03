def selection_sort_partial_count(arr, k):
    n = len(arr)
    comparisons = 0
    for i in range(min(k, n)):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return comparisons


def insertion_sort_count(arr, start):
    n = len(arr)
    comparisons = 0
    for i in range(start, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        comparisons += (
            1 if j >= 0 else 0
        )  # Account for the final comparison when while loop ends
    return comparisons


def hybrid_sort_with_optimal_k(arr):
    n = len(arr)
    min_comparisons = float("inf")
    optimal_k = 0
    best_sorted_arr = arr.copy()

    # Try all possible values of k
    for k in range(n + 1):
        temp_arr = arr.copy()

        # Count comparisons for Selection Sort
        selection_comparisons = selection_sort_partial_count(temp_arr, k)

        # Count comparisons for Insertion Sort
        insertion_comparisons = insertion_sort_count(temp_arr, k)

        # Total comparisons
        total_comparisons = selection_comparisons + insertion_comparisons

        # Update if this k gives fewer comparisons
        if total_comparisons < min_comparisons:
            min_comparisons = total_comparisons
            optimal_k = k
            best_sorted_arr = temp_arr.copy()

    return best_sorted_arr, optimal_k, min_comparisons


def solve(nums):
    # Write code here
    sorted_arr, optimal_k, total_comparisons = hybrid_sort_with_optimal_k(nums)
    print(" ".join(map(str, sorted_arr)))
