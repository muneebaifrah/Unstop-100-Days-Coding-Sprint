# Read input
n = int(input().strip())
binary_digits = list(map(int, input().split()))

# Convert binary list to string
binary_string = ''.join(map(str, binary_digits))

# Convert binary string to decimal
decimal_value = int(binary_string, 2)

# Print result
print(decimal_value)