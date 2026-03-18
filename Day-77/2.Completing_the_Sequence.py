def min_insertions_to_make_valid_pqr(s):
    pattern = "PQR"
    i = 0  # Pointer for input string
    j = 0  # Pointer for pattern
    insertions = 0
    n = len(s)

    while i < n:
        if s[i].upper() == pattern[j]:
            i += 1
        else:
            # Insert the expected character
            insertions += 1
        j = (j + 1) % 3

    # After processing, if we didn't end exactly at the end of a "PQR" group
    if j != 0:
        insertions += (3 - j)

    return insertions

# Input handling
def main():
    N = int(input())
    s = input().strip()
    print(min_insertions_to_make_valid_pqr(s))

if __name__ == "__main__":
    main()