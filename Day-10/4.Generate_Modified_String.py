def modify_string(n, s):
    primes = {2, 3, 5, 7}
    prime_values = []

    # Step 1 & 2: collect prime digits
    for ch in s:
        if ch.isdigit():
            val = int(ch)
            if val in primes:
                prime_values.append(val)

    # Step 3: compute unique number
    if prime_values:
        unique_number = sum(prime_values) // len(prime_values)
    else:
        unique_number = None  # indicates no primes present

    # Step 4: build modified string
    result = []

    for ch in s:
        if ch.isdigit():
            digit = int(ch)
            if unique_number is not None:
                index = digit % unique_number
            else:
                index = digit
            result.append(chr(ord('a') + index))
        else:
            result.append(ch)

    return ''.join(result)


if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    s = data[1]
    
    print(modify_string(n, s))
