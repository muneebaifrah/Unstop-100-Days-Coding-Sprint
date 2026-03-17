def distinct_strings_after_removal(s):
    n = len(s)
    distinct = set()
    
    for i in range(n - 1):
        # Remove s[i] and s[i+1]
        new_str = s[:i] + s[i+2:]
        distinct.add(new_str)
    
    return len(distinct)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().strip()
        print(distinct_strings_after_removal(S))