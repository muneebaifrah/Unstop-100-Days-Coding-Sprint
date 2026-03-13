# Enter your code here. Read input from STDIN. Print output to STDOUT
def reverse_parentheses(s: str) -> str:
    n = len(s)
    stack = []
    pair = [0] * n
    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            j = stack.pop()
            pair[i] = j
            pair[j] = i
    res = []
    i = 0
    d = 1
    
    while i < n:
        if s[i] == '(' or s[i] == ')':
            i = pair[i]
            d = -d
        else:
            res.append(s[i])
        i += d
    
    return ''.join(res)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read().strip()
    print(reverse_parentheses(input))