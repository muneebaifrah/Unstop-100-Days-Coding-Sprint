def frequency_sort(s):
    freq = {}
    first_index = {}

    for i, ch in enumerate(s):
        if ch not in freq:
            freq[ch] = 0
            first_index[ch] = i
        freq[ch] += 1

    # sort by frequency descending, first occurrence ascending
    chars = sorted(freq.keys(), key=lambda x: (-freq[x], first_index[x]))

    result = []
    for ch in chars:
        result.append(ch * freq[ch])

    return "".join(result)


# Input
s = input().strip()

print(frequency_sort(s))