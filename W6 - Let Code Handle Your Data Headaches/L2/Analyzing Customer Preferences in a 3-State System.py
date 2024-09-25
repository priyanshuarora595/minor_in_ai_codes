def matrix_factorization_3state(E0, M0, H0, transition_matrix):
    # define threshold
    threshold = 0.0001

    # Initialize the current distribution
    distribution = [E0, M0, H0]

    # Initialize iteration counter
    iterations = 0

    while True:
        # Calculate the new distribution
        new_distribution = [
            sum(distribution[j] * transition_matrix[i][j] for j in range(3))
            for i in range(3)
        ]

        # Check for convergence
        if (
            max(abs(new_distribution[i] - distribution[i]) for i in range(3))
            < threshold
        ):
            break

        # Update the distribution for the next iteration
        distribution = new_distribution

        # Increment the iteration counter
        iterations += 1

    # Print results
    print(iterations)
    print(" ".join(f"{x:.4f}" for x in distribution))
