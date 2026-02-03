def calculate_f_score(features, N):
    result = 0
    for i in range(N):
        if ((i + 1) * (N - i)) % 2 == 1:
            result ^= features[i]
    return result


N = int(input().strip())
features = list(map(int, input().split()))
print(calculate_f_score(features, N))
