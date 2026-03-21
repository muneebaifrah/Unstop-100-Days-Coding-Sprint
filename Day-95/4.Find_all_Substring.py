def find_repeated_substrings(s):
    n = len(s)
    if n < 10:
        return

    freq = {}
    order = []

    # Sliding window of size 10
    for i in range(n - 9):
        sub = s[i:i+10]
        if sub not in freq:
            freq[sub] = 1
            order.append(sub)
        else:
            freq[sub] += 1

    # Print substrings that occurred more than once
    result = [sub for sub in order if freq[sub] > 1]
    print(" ".join(result))


# -------- Driver Code --------
s = input().strip()
find_repeated_substrings(s)