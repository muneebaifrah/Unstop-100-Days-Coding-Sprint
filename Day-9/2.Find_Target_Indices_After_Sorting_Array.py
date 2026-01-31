N = int(input())
A = list(map(int, input().split()))
K = int(input())

A.sort()

indices = [i for i, val in enumerate(A) if val == K]

print(len(indices))
if indices:
    print(*indices)
