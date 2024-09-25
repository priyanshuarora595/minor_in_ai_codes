def matrix_factorization_2state(E0, M0, time_periods):
    """
    Kindly note:
    There is no need of taking any input. You can find the initial market shares as E0 & M0 and
    Time periods as time_periods. These are the functions parameters & you need to use them to
    complete this function.
    Additionally, you need to print the output as mentioned in the problem and there is no need
    of returning anything from the function.
    """
    # Initialize market shares
    market_shares = [E0, M0]

    # Transition matrix for the Markov Chain
    transition_matrix = [
        [0.50, 0.25],  # From Region A to A and B
        [0.50, 0.75],  # From Region B to A and B
    ]

    for i in range(1, time_periods + 1):
        # Calculate new market shares
        new_shares = [
            market_shares[0] * transition_matrix[0][0]
            + market_shares[1] * transition_matrix[1][0],
            market_shares[0] * transition_matrix[0][1]
            + market_shares[1] * transition_matrix[1][1],
        ]

        # Update market shares
        market_shares = new_shares

        # Store the formatted results
        print(
            f"After iteration {i}: E = {market_shares[0]:.4f}, M = {market_shares[1]:.4f}"
        )

    # Print the final market share
    print(f"Final market shares after {time_periods} iterations:")
    print(f"Region A = {market_shares[0]:.4f}, Region B = {market_shares[1]:.4f}")
