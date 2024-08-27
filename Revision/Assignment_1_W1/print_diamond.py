def print_diamond(n):
    # Upper part of the diamond (including the middle)
    for i in range(1, n + 1):
        # Print leading spaces
        spaces = n - i
        # Print stars
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

    # Lower part of the diamond (after the middle)
    for i in range(n - 1, 0, -1):
        # Print leading spaces
        spaces = n - i
        # Print stars
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)
