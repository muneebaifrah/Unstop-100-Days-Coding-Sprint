from collections import Counter

def longest_palindrome(s):
    res = ""
    
    for i in range(len(s)):
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
        
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r-l+1 > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1
            
    return res


def min_window(s, t):
    need = Counter(t)
    missing = len(t)
    left = start = end = 0
    
    for right, ch in enumerate(s, 1):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            start, end = left, right
            return end - start
    
    return float('inf')


def user_logic(str1, str2, k):
    str1_ = longest_palindrome(str1)
    str2_ = longest_palindrome(str2)
    
    length = min_window(str1_, str2_)
    
    if length >= k and length != float('inf'):
        return "YES"
    return "NO"


# ---- Input Handling ----
str1, str2 = input().split()
k = int(input())

print(user_logic(str1, str2, k))