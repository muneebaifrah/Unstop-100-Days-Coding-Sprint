MOD = 998244353

def count_valid_ways(cards):
    """
    Write your logic here.
    Parameters:
        cards (list of tuples): List of tuples where each tuple contains two integers (A_i, B_i)
    Returns:
        int: Number of valid ways to flip the cards such that no two adjacent cards show the same number
    """
    n = len(cards)
    # dp[i][0] -> If i-th card is face-up (Ai)
    # dp[i][1] -> If i-th card is face-down (Bi)
    dp = [[0, 0] for _ in range(n)]
    
    # Base case: First card can be placed in one way for each side
    dp[0][0] = 1
    dp[0][1] = 1
    
    for i in range(1, n):
        Ai, Bi = cards[i]
        A_prev, B_prev = cards[i-1]
        
        # If Ai is visible
        if Ai != A_prev:
            dp[i][0] += dp[i-1][0]
        if Ai != B_prev:
            dp[i][0] += dp[i-1][1]

        # If Bi is visible
        if Bi != A_prev:
            dp[i][1] += dp[i-1][0]
        if Bi != B_prev:
            dp[i][1] += dp[i-1][1]
        
        # Apply modulo
        dp[i][0] %= MOD
        dp[i][1] %= MOD

    # Final answer: sum both cases
    return (dp[n-1][0] + dp[n-1][1]) % MOD


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    cards = []
    index = 1
    for i in range(n):
        a = int(data[index])
        b = int(data[index + 1])
        cards.append((a, b))
        index += 2
    
    # Call user logic function and print the output
    result = count_valid_ways(cards)
    print(result)

if __name__ == "__main__":
    main()