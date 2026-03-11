def user_logic(arr):
    stack = []
    result = 0
    
    for num in arr:
        # While top of stack is smaller than current number
        while stack and stack[-1] <= num:
            mid = stack.pop()
            # Multiply mid with the smaller of its two neighbors
            if stack:
                result += mid * min(stack[-1], num)
            else:
                result += mid * num
        stack.append(num)
    
    # Remaining elements in stack — multiply adjacent pairs
    while len(stack) > 1:
        result += stack[-1] * stack[-2]
        stack.pop()
    
    return result

def main():
    import sys
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    print(user_logic(arr))

if __name__ == "__main__":
    main()
                