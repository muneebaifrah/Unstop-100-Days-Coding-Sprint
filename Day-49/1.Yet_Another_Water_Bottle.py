def water_jug(X, i, j):
    """
    Write your logic here.
    Parameters:
        X (float): Total amount of water
        i (int): Row number
        j (int): Bottle number in the row
    Returns:
        float: Amount of water in the j-th bottle of the i-th row
    """
    # Initialize a 2D list to store water in each bottle
    # We only need to simulate up to row i
    dp = [[0.0 for _ in range(row + 1)] for row in range(i)]
    
    # Pour all water into the top bottle
    dp[0][0] = X

    # Simulate overflow row by row
    for row in range(i - 1):
        for col in range(row + 1):
            if dp[row][col] > 1.0:
                overflow = dp[row][col] - 1.0
                dp[row][col] = 1.0
                dp[row + 1][col] += overflow / 2.0
                dp[row + 1][col + 1] += overflow / 2.0

    # Return the amount in the j-th bottle of the i-th row
    # Adjusting for 0-based indexing
    return min(1.0, dp[i - 1][j - 1])

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    i = int(data[0])  # First input is the integer i (row number)
    j = int(data[1])  # Second input is the integer j (bottle number in the row)
    X = float(data[2])  # Third input is the floating number X (total amount of water)
    
    # Call user logic function and print the output with 6 decimal places
    result = water_jug(X, i, j)
    print(f"{result:.6f}")

if __name__ == "__main__":
    main()
                