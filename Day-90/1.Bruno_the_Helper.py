import sys
from collections import Counter

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N, X = map(int, input().split())
    arr = list(map(int, input().split()))
    
    freq = Counter(arr)
    
    total_sum = 0
    found = False
    
    for num, count in freq.items():
        if count == X:
            total_sum += num
            found = True
    
    print(total_sum if found else -1)