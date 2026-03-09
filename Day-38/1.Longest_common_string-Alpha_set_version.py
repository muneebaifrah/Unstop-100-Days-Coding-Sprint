from collections import Counter
import sys

def longest_common_alpha_string_length(strings):
    # Initialize with infinity counts for each char
    min_freq = [float('inf')] * 26
    
    for s in strings:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        # Update min frequency across all strings
        for i in range(26):
            min_freq[i] = min(min_freq[i], freq[i])
    
    # Answer is sum of min frequencies
    return sum(f for f in min_freq if f != float('inf'))

# Input reading
if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split()
    N = int(input_data[0])
    strings = input_data[1:]
    
    result = longest_common_alpha_string_length(strings)
    print(result)
                