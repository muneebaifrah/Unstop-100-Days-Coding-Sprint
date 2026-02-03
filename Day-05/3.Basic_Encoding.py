q = int(input())
freq = {}

for _ in range(q):
    a, b = map(int, input().split())
    freq[b] = freq.get(b, 0) + a

if len(freq) <= 1:
    print(0)
else:
    min_freq = min(freq.values())
    max_freq = max(freq.values())
    
    min_numbers = [num for num, f in freq.items() if f == min_freq]
    max_numbers = [num for num, f in freq.items() if f == max_freq]
    
    low = min(min_numbers)
    high = max(max_numbers)
    
    print(abs(high - low))
