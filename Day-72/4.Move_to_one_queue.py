n = int(input().strip())
pos = list(map(int, input().split()))

even_count = sum(1 for x in pos if x % 2 == 0)
odd_count  = n - even_count

# minimum cost
print(min(n - even_count, n - odd_count))