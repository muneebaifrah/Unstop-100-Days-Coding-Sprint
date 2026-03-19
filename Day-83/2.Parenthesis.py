def is_magical(s: str) -> bool:
    stack = []
    # Mapping of closing powers to their corresponding opening powers
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            # If stack is empty or top of stack is not the matching opening power
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    # If stack is empty, all opening powers are properly closed
    return len(stack) == 0

# Read input string
s = input().strip()

# Print True or False based on the magical string check
print(is_magical(s))