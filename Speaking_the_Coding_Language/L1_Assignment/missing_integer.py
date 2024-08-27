def find_missing_number(numbers):
    """
    You are not required to take input for the list.
    Input list is already given as numbers. You just
    need to use it for the program.
    """
    # Write code here
    s = sum(numbers)
    n = len(numbers) + 1
    actual_sum = (n * (n + 1)) // 2
    return actual_sum - s
