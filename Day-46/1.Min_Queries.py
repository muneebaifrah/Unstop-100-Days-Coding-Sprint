def user_logic(n, m, arr, queries):
    
    prefixMin = [0] * n
    prefixMin[0] = arr[0]

    for i in range(1, n):
        prefixMin[i] = min(prefixMin[i-1], arr[i])

    result = []

    for q in queries:
        result.append(prefixMin[q])

    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    ans = user_logic(n, m, arr, queries)
    print(*ans)