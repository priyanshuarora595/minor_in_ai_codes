def calculate_median(scores):
    sorted_scores = sorted(scores)

    n = len(sorted_scores)
    mid = n // 2

    # Calculate median based on the number of elements
    if n % 2 == 1:
        return sorted_scores[mid]
    else:
        return (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
