import sys
input = sys.stdin.readline

MOD = 10**9 + 7

N = int(input().strip())

# Special case
if N == 0:
    print(1)
    exit()

# Initial counts for length 1
a = e = i = o = u = 1

for _ in range(2, N + 1):
    new_a = (e + u) % MOD
    new_e = (a + i) % MOD
    new_i = (e + o) % MOD
    new_o = (i + u) % MOD
    new_u = (a + o) % MOD
    
    a, e, i, o, u = new_a, new_e, new_i, new_o, new_u

total = (a + e + i + o + u) % MOD

# Convert to octal
print(oct(total)[2:])