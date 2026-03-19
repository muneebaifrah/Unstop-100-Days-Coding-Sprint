def will_police_be_alerted():
    import sys
    input = sys.stdin.readline

    # Read input
    N, K, X = map(int, input().split())
    speeds = list(map(int, input().split()))

    # Sort the speeds
    speeds.sort()

    count = 0
    j = 0

    # Two pointer technique
    for i in range(N):
        while j < N and speeds[j] - speeds[i] < K:
            j += 1
        # All pairs (i, j), where j > i and speeds[j] - speeds[i] >= K
        count += N - j

    print("YES" if count > X else "NO")

# Run the function
will_police_be_alerted()