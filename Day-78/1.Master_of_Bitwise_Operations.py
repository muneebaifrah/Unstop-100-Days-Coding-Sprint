import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, Q = map(int, input().split())
    A = [0] + list(map(int, input().split()))

    pref = [[0]*(N+1) for _ in range(31)]

    for b in range(31):
        for i in range(1, N+1):
            pref[b][i] = pref[b][i-1] + ((A[i] >> b) & 1)

    for _ in range(Q):
        k, X1, Y1, X2, Y2 = map(int, input().split())

        ones1 = pref[k][Y1] - pref[k][X1-1]
        ones2 = pref[k][Y2] - pref[k][X2-1]

        len1 = Y1 - X1 + 1
        len2 = Y2 - X2 + 1

        zeros1 = len1 - ones1
        zeros2 = len2 - ones2

        ans = ones1 * zeros2 + zeros1 * ones2
        print(ans)