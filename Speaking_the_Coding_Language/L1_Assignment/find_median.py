def calculate_median(scores):
    """
    You are not required to take input for the scores.
    You just need to use `scores` variable to complete
    the program.
    """
    # Write code here
    scores = sorted(scores)
    l = len(scores)
    if l % 2 == 0:
        a = scores[l // 2]
        b = scores[(l // 2) - 1]
        return (a + b) / 2
    return scores[l // 2]
