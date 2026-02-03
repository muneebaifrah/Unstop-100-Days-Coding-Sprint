n = int(input())
fruits = list(map(int, input().split()))
fruits.sort()
print(sum(fruits[i] for i in range(0, n, 2)))
