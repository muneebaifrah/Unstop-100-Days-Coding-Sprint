import sys
sys.setrecursionlimit(10**7)

def longest_palindromic_substring_length(n, s):
    # Manacher's Algorithm
    
    # Transform string
    t = ['#'] * (2 * n + 1)
    for i in range(n):
        t[2 * i + 1] = s[i]
    
    P = [0] * (2 * n + 1)
    center = 0
    right = 0
    max_len = 0
    
    for i in range(2 * n + 1):
        mirror = 2 * center - i
        
        if i < right:
            P[i] = min(right - i, P[mirror])
        
        # Expand
        while (i - P[i] - 1 >= 0 and
               i + P[i] + 1 < 2 * n + 1 and
               t[i - P[i] - 1] == t[i + P[i] + 1]):
            P[i] += 1
        
        if i + P[i] > right:
            center = i
            right = i + P[i]
        
        max_len = max(max_len, P[i])
    
    return max_len


# ---- Input Handling ----
if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1]
    
    print(longest_palindromic_substring_length(n, s))
