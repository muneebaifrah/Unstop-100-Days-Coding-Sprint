def normalize(s):
    mapping = {}
    res = []
    counter = 0
    for ch in s:
        if ch not in mapping:
            mapping[ch] = counter
            counter += 1
        res.append(mapping[ch])
    return res

def find_and_replace_pattern(words, pattern):
    pattern_norm = normalize(pattern)
    matched = []
    
    for word in words:
        if len(word) != len(pattern):
            continue
        if normalize(word) == pattern_norm:
            matched.append(word)
    
    print(len(matched))
    print(" ".join(matched))

# Read input
N = int(input())
words = input().split()
pattern = input()

# Find matches
find_and_replace_pattern(words, pattern)