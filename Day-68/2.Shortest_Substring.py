from collections import Counter

def shortestSubstring(S, L):
    need = Counter(L)
    have = Counter()
    required = len(need)
    formed = 0
    
    left = 0
    min_len = float('inf')
    
    for right, ch in enumerate(S):
        have[ch] += 1
        if ch in need and have[ch] == need[ch]:
            formed += 1
        
        # Try to shrink window
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
            
            # Remove left char
            have[S[left]] -= 1
            if S[left] in need and have[S[left]] < need[S[left]]:
                formed -= 1
            left += 1
    
    return min_len if min_len != float('inf') else -1


# Driver
if __name__ == "__main__":
    S = input().strip()
    L = input().strip()
    print(shortestSubstring(S, L))