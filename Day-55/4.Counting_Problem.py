import heapq
from collections import Counter

def count_unique_numbers(arr):
    """
    Determines the count of unique numbers based on the given conditions.
    
    Parameters:
        arr (list): List of integers
    
    Returns:
        int: Count of unique numbers based on the problem statement
    """
    if not arr:
        return 0

    # Step 1: Count frequencies
    freq = Counter(arr)
    
    # Step 2: Use a max-heap (Python heapq is min-heap, so use negative values)
    max_heap = [-num for num in freq.keys()]
    heapq.heapify(max_heap)
    
    unique_count = 0  # Count of unique numbers

    while max_heap:
        num = -heapq.heappop(max_heap)  # Get the largest number
        
        if freq[num] == 1:  # Unique number
            unique_count += 1
            del freq[num]  # Remove from frequency map
            
            # Insert half of num if it's greater than zero
            half_num = num // 2
            if half_num > 0:
                if half_num in freq:
                    freq[half_num] += 1
                else:
                    freq[half_num] = 1
                    heapq.heappush(max_heap, -half_num)  # Insert in heap
                
        else:  # Non-unique, remove all occurrences
            del freq[num]
    
    return unique_count

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Read N
    arr = list(map(int, data[1:]))  # Read array
    
    # Compute and print result
    print(count_unique_numbers(arr))

if __name__ == "__main__":
    main()