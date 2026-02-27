def matching_count(items, ruleKey, ruleValue):
    # Map ruleKey to the correct index
    key_index = {'type': 0, 'color': 1, 'name': 2}
    idx = key_index[ruleKey.strip()]  # Remove extra spaces
    
    count = 0
    for item in items:
        if item[idx].strip() == ruleValue.strip():  # Remove extra spaces
            count += 1
    return count

# Read input
n = int(input())
items = [input().split() for _ in range(n)]
ruleKey = input().strip()
ruleValue = input().strip()

# Compute result
result = matching_count(items, ruleKey, ruleValue)
print(result)