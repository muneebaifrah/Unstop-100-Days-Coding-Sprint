import sys
input = sys.stdin.readline

# Read inputs
K = int(input().strip())
N = int(input().strip())

if N == 0:
    print("null")
    sys.exit()

arr = list(map(int, input().split()))

# Special case: if K > N, return original list
if K > N:
    for val in arr:
        print(val, end=" --> ")
    print("null")
    sys.exit()

result = []
i = 0

while i < N:
    # If remaining elements are less than K
    if i + K > N:
        result.extend(arr[i:])
        break
    else:
        group_sum = sum(arr[i:i+K])
        mean = group_sum // K
        result.append(mean)
        i += K

# Print result in required format
for val in result:
    print(val, end=" --> ")
print("null")