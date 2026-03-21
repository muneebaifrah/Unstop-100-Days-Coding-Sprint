import sys

def min_difficulty(arr, d):
    n = len(arr)
    
    if n < d:
        return -1
    
    # dp[day][i] = min difficulty to finish first i jobs in 'day' days
    # we optimize to 2 rows
    prev = [float('inf')] * (n + 1)
    prev[0] = 0
    
    for day in range(1, d + 1):
        curr = [float('inf')] * (n + 1)
        
        for i in range(day, n + 1):
            max_d = 0
            # last partition: jobs[j..i-1]
            for j in range(i - 1, day - 2, -1):
                max_d = max(max_d, arr[j])
                curr[i] = min(curr[i], prev[j] + max_d)
        
        prev = curr
    
    return prev[n]


if __name__ == "__main__":
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    B = data[0]
    arr = data[1:1+B]
    D = data[1+B]
    
    print(min_difficulty(arr, D))