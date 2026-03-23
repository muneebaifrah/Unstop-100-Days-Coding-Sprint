# Enter your code here. Read input from STDIN. Print output to STDOUT
def count_subsequences(S, query):
    """
    Counts how many times 'query' appears as a subsequence in 'S'.

    Parameters:
        S (str): The source string.
        query (str): The target subsequence.

    Returns:
        int: Number of times query appears as a subsequence in S.
    """
    n, m = len(S), len(query)
    dp = [0] * (m + 1)
    dp[0] = 1  # Empty query is a subsequence of any prefix

    for i in range(n):
        for j in range(m, 0, -1):
            if S[i] == query[j - 1]:
                dp[j] += dp[j - 1]
    return dp[m]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    S = data[0]
    query = data[1]
    result = count_subsequences(S, query)
    print(result)

if __name__ == "__main__":
    main()