def user_logic(capacity, operations):
    stack = []
    result = ["null"]  # Initialization step always returns "null"

    for op in operations:
        parts = op.split()
        
        if parts[0] == "push":
            if len(stack) < capacity:
                stack.append(int(parts[1]))
            # push always returns "null"
            result.append("null")
            
        elif parts[0] == "pop":
            if stack:
                result.append(str(stack.pop()))
            else:
                result.append("-1")
                
        elif parts[0] == "increment":
            k = int(parts[1])
            inc = int(parts[2])
            for i in range(min(k, len(stack))):
                stack[i] += inc
            # increment always returns "null"
            result.append("null")
    
    return result


# Read input
capacity = int(input().strip())
q = int(input().strip())
operations = [input().strip() for _ in range(q)]

# Execute
output = user_logic(capacity, operations)
print(" ".join(output))