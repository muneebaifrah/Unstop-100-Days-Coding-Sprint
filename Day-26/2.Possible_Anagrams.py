def find_anagram_indices(secret1, secret2):
    from collections import Counter

    len_s1 = len(secret1)
    len_s2 = len(secret2)

    if len_s2 > len_s1:
        print("Empty Array")
        return

    # Count characters in secret2
    count_s2 = Counter(secret2)
    # Count characters in the current window of secret1
    window_count = Counter(secret1[:len_s2])

    result = []

    # Check the first window
    if window_count == count_s2:
        result.append(0)

    # Slide the window
    for i in range(1, len_s1 - len_s2 + 1):
        out_char = secret1[i-1]
        window_count[out_char] -= 1
        if window_count[out_char] == 0:
            del window_count[out_char]

        in_char = secret1[i + len_s2 - 1]
        window_count[in_char] += 1

        if window_count == count_s2:
            result.append(i)

    if result:
        print(" ".join(map(str, result)))
    else:
        print("Empty Array")


# Read input from stdin
secret1 = input().strip()
secret2 = input().strip()

find_anagram_indices(secret1, secret2)