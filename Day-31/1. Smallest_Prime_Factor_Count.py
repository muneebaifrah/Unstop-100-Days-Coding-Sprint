from bisect import bisect_left, bisect_right
import sys

MAXN = 100005
cnt = [[] for _ in range(MAXN)]
spf = [0] * MAXN
prefix_sum = [[] for _ in range(MAXN)]

# Function to initialize the smallest prime factor and count arrays
def init(n=100000):
    for i in range(2, n + 1):
        for k in range(i, n + 1, i):
            if spf[k] == 0:
                spf[k] = i
                cnt[i].append(k)
    
    # Create prefix sum arrays for each prime factor
    for i in range(2, n + 1):
        if cnt[i]:
            prefix_sum[i] = [0] * (len(cnt[i]) + 1)
            for j in range(1, len(cnt[i]) + 1):
                prefix_sum[i][j] = prefix_sum[i][j - 1] + 1


def user_logic(p, L, R):
    """
    Write your logic here.
    Parameters:
        p (int): A prime number
        L (int): The inclusive lower bound of the range
        R (int): The inclusive upper bound of the range
    Returns:
        int: Computed result based on the problem statement
    """ 
    lower = bisect_left(cnt[p], L)
    upper = bisect_right(cnt[p], R) 
    return (prefix_sum[p][upper] - prefix_sum[p][lower])
    pass

def main():
    input = sys.stdin.read
    data = input().split()
    
    init()  # Initialize with the default value of 100000

    Q = int(data[0])
    index = 1
    results = []
    for _ in range(Q):
        p = int(data[index])
        L = int(data[index + 1])
        R = int(data[index + 2])
        index += 3

        result = user_logic(p, L, R)
        results.append(result)
   
    for result in results:
        print(result)

if __name__ == "__main__":
    main()