n = int(input().strip())

# Check if n is a power of 2
if n > 0 and (n & (n - 1)) == 0:
    print("YES")
else:
    print("NO")