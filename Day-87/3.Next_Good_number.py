import sys

# Fast input
input = sys.stdin.read

# Read all inputs at once
data = input().split()

# First input is T
T = int(data[0])

# Store results
results = []

# Predefine a set of odd digits for quick lookup
odd_digits = {'1', '3', '5', '7', '9'}

# Function to check if all digits of a number are odd
def is_good(num):
    return all(d in odd_digits for d in str(num))

# Process each test case
for i in range(1, T + 1):
    x = int(data[i])
    x += 1
    while not is_good(x):
        x += 1
    results.append(str(x))

# Print all results at once
sys.stdout.write('\n'.join(results) + '\n')