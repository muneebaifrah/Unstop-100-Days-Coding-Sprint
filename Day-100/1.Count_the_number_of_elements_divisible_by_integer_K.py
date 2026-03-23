from itertools import permutations

def count_divisible_combinations(K, N, arr):
    seen = set()

    for r in range(1, N+1):
        for p in permutations(arr, r):
            num = int(''.join(map(str, p)))
            if num % K == 0:
                seen.add(num)

    return len(seen)


if __name__ == '__main__':
    K = int(input())
    N = int(input())
    arr = list(map(int, input().split()))
    result = count_divisible_combinations(K, N, arr)
    print(result)