def cycle_end(n, k):
    ans = 0
    for i in range(2, n + 1):
        ans = (ans + k) % i
    return ans


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(cycle_end(n, k))