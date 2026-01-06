def user_logic(ops):
    stack = []

    for op in ops:
        if op == '+':
            x = stack[-1]
            y = stack[-2]

            stack.append(x+y)

        elif op == 'D':
            stack.append(2 * stack[-1])
        
        elif op == 'C':
            stack.pop()

        else:
            stack.append(int(op))
    
    return sum(stack)
    

if __name__ == "__main__":
    n = int(input())  # Input for number of operations
    ops = input().split()
    
    # Call user logic function and print the output
    result = user_logic(ops)
    print(result)