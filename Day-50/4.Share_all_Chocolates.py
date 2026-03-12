def can_partition_chocolates(n, chocolates):
    # Step 1: Compute total sum of chocolates
    total_sum = sum(chocolates)
    
    # Step 2: If sum is odd, we can't divide into two equal parts
    if total_sum % 2 != 0:
        return "NO"
    
    # Step 3: We need to find a subset with sum = total_sum // 2
    target = total_sum // 2
    
    # Step 4: DP approach (subset sum problem)
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: sum of 0 is always possible
    
    for choc in chocolates:
        for j in range(target, choc - 1, -1):
            dp[j] = dp[j] or dp[j - choc]
    
    # Step 5: Check if we can form subset with sum = total_sum / 2
    return "YES" if dp[target] else "NO"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    chocolates = list(map(int, data[1:]))  # Remaining input is the array of chocolates
    
    # Call user logic function and print the output
    result = can_partition_chocolates(n, chocolates)
    print(result)

if __name__ == "__main__":
    main()