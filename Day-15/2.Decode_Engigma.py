def interpret(s):
    mapping = {
        "S": "send",
        "[]": "the",
        "[sps]": "ships"
    }
    
    result = []
    i = 0
    n = len(s)
    
    while i < n:
        if s[i] == 'S':
            result.append("send")
            i += 1
        elif s[i] == '[':
            if i + 1 < n and s[i+1] == ']':
                result.append("the")
                i += 2
            elif i + 4 < n and s[i+1:i+4] == 'sps' and s[i+4] == ']':
                result.append("ships")
                i += 5
        else:
            # Should not happen based on problem constraints
            i += 1
    
    # Join all words with a space
    print(" ".join(result))


# Example usage
s = input()
interpret(s)