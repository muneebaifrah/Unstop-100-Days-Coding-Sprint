import sys
from collections import defaultdict
from bisect import bisect_left

def count_pairs_subarrays():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    arr = list(map(int, input_data[1:]))
    
    sum_map = defaultdict(list)
    prefix_sum = 0
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i+1] = prefix_sums[i] + arr[i]

    for l in range(n):
        for r in range(l, n):
            sub_sum = prefix_sums[r+1] - prefix_sums[l]
            sum_map[sub_sum].append((l, r))
            
    ans = 0
    
    for sub_sum in sum_map:
        intervals = sum_map[sub_sum]
        if len(intervals) < 2:
            continue
            
        
        all_ends = sorted(it[1] for it in intervals)
        
        for l_curr, r_curr in intervals:
            count = bisect_left(all_ends, l_curr)
            ans += count
            
    print(ans)

if __name__ == "__main__":
    count_pairs_subarrays()