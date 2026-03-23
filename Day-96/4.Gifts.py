import sys

MOD = 10**9 + 7

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    
    friends = []
    for _ in range(N):
        data = list(map(int, input().split()))
        k = data[0]
        gifts = data[1:]
        friends.append(gifts)
    
    # dp[mask] = number of ways to assign gifts to friends represented by mask
    # mask: which friends have already been assigned
    dp = [0] * (1 << N)
    dp[0] = 1
    
    # For each gift ID from 1 to 200, try assigning it
    for gift_id in range(1, 201):
        # For this gift, find which friends have it
        available = []
        for i in range(N):
            if gift_id in friends[i]:
                available.append(i)
        
        if not available:
            continue
        
        new_dp = dp[:]
        
        for mask in range(1 << N):
            if dp[mask] == 0:
                continue
            for friend in available:
                if not (mask & (1 << friend)):
                    new_mask = mask | (1 << friend)
                    new_dp[new_mask] = (new_dp[new_mask] + dp[mask]) % MOD
        
        dp = new_dp
    
    print(dp[(1 << N) - 1] % MOD)

if __name__ == "__main__":
    main()