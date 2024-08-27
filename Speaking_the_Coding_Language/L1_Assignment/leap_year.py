def is_leap_year(date_string):
    """
    You are not required to take input.
    `date_string` is already given to you.
    You just need to use it and return the
    boolean value accordingly.
    """
    # Write code here
    year = int(date_string[:4])

    # Leap year conditions
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
