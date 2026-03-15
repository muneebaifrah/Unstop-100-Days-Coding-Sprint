def user_logic(n):
    """
    Write your logic here.
    Parameters:
        n (int): Number of pairs of people who need to be mutual Probab-list friends
    Returns:
        tuple: A tuple containing two integers (min_people, max_one_way_pairs)
    """
    # Placeholder for user logic

    if n == 0:
        return (0, 0)

    # Precompute triangular numbers T(k) = k*(k-1)//2 for k >= 2 and <= n
    coins = []
    k = 2
    while True:
        val = k * (k - 1) // 2
        if val > n:
            break
        coins.append((k, val))
        k += 1

    INF = 10**9
    dp = [INF] * (n + 1)
    dp[0] = 0

    # DP: dp[x] = minimum people needed to achieve exactly x mutual pairs
    for x in range(1, n + 1):
        for cost, val in coins:
            if val > x:
                break
            if dp[x - val] + cost < dp[x]:
                dp[x] = dp[x - val] + cost

    min_people = dp[n]
    max_one_way_pairs = (min_people * (min_people - 1)) // 2 - n
    return (min_people, max_one_way_pairs)


def main():
    import sys
    data = sys.stdin.read().strip()
    n = int(data)
    min_people, max_one_way_pairs = user_logic(n)
    print(f"{min_people} {max_one_way_pairs}")


if __name__ == "__main__":
    main()




'''
import sys
input = sys.stdin.read
data = input().strip()
n = int(data)  # Read the value of N from the input
min_people, max_one_way_pairs = user_logic(n)
print("{} {}".format(min_people, max_one_way_pairs))
'''