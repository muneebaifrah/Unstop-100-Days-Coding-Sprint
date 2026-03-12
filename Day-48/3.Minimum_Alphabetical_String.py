def lex_smallest_string(n, k):
    # Initialize with 'a'
    res = ['a'] * n
    extra = k - n
    
    # Fill from the right
    i = n - 1
    while extra > 0:
        add = min(25, extra)
        res[i] = chr(ord('a') + add)
        extra -= add
        i -= 1
    
    return ''.join(res)

# Read input
n, k = map(int, input().split())
print(lex_smallest_string(n, k))