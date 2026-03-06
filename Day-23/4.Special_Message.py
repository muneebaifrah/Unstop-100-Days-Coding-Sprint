import re

# Read input string
S = input().strip()

# Read number of key-value pairs
N = int(input())

# Read key-value pairs into a dictionary
kv = {}
for _ in range(N):
    line = input().rstrip()
    if ' ' in line:
        key, value = line.split(' ', 1)
    else:
        key, value = line, ""
    kv[key] = value

# Function to replace acronyms
def replace_acronym(match):
    key = match.group(1)
    return kv.get(key, "?")

# Replace all acronyms using regex
pattern = r'\((.*?)\)'
result = re.sub(pattern, replace_acronym, S)

# Print final result
print(result)
                