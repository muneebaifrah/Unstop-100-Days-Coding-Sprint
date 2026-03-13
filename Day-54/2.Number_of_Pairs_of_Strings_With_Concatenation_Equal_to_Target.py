def count_valid_pairs(nums, target):
    count = 0
    n = len(nums)
    
    # Check all pairs (i, j) where i ≠ j
    for i in range(n):
        for j in range(n):
            if i != j and nums[i] + nums[j] == target:
                count += 1
                
    return count

# Read input
n = int(input())  # Size of array
nums = input().split()  # Array elements as strings
target = input().strip()  # Target string

# Call function and print result
print(count_valid_pairs(nums, target))