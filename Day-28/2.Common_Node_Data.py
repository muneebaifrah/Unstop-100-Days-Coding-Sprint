# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = n - 1
j = m - 1

last_common = -1

while i >= 0 and j >= 0 and a[i] == b[j]:
    last_common = a[i]
    i -= 1
    j -= 1

print(last_common)