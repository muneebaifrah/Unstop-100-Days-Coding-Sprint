def min_total_vulnerability(N, K, arr):
    # dp[i] represents the minimum sum of vulnerabilities for subarray arr[0...i-1]
    dp = [float('inf')] * (N + 1)
    dp[0] = 0  # base case: no subarray, no vulnerability
    
    # Process each position in the array
    for i in range(1, N + 1):
        # We consider subarrays of length at most K
        max_vul = 0
        # Try different subarray lengths ending at index i
        for j in range(1, min(K, i) + 1):
            # Update the maximum vulnerability in the subarray arr[i-j...i-1]
            max_vul = max(max_vul, arr[i - j])
            dp[i] = min(dp[i], dp[i - j] + max_vul)
    
    # The minimum total sum of vulnerabilities is stored in dp[N]
    return dp[N]

# Read input
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# Output the result
print(min_total_vulnerability(N, K, arr))