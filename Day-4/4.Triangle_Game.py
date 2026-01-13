n = int(input())
row = [1]
for _ in range(n):
    row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
print(*row)