n,m = map(int, input().split())
incoming = [0] * (n+1)
outgoing = [0] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    outgoing[a] += 1
    incoming[b] += 1
ans = -1
for i in range (1, n+1):
        if outgoing[i] == 0 and incoming[i] == n-1:
            ans = i
            break
print(ans)