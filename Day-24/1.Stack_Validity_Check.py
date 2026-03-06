def validate_stack_sequences(pushed, popped):
    stack = []
    j = 0  # index for popped

    # simulate stack operations
    for x in pushed:
        stack.append(x)
        # pop while top matches popped[j]
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1

    # if all popped elements matched
    if j == len(popped):
        return True, 0

    # otherwise invalid → count primes <= remaining stack size
    remaining = len(stack)

    def count_primes(n):
        if n < 2:
            return 0
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n + 1, i):
                    is_prime[j] = False

        return sum(is_prime)

    return False, count_primes(remaining)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    pushed = list(map(int, data[1:n+1]))  # Next n integers are the pushed sequence
    popped = list(map(int, data[n+1:2*n+1]))  # Next n integers are the popped sequence
    
    # Call user logic function
    is_valid, prime_count = validate_stack_sequences(pushed, popped)
    
    # Print the output based on the returned values
    if is_valid:
        print("true")
    else:
        print("false")
        print(prime_count)

if __name__ == "__main__":
    main()
                