def to_excel_column(n):
    """Convert number to Excel column name."""
    result = []
    while n > 0:
        n -= 1
        result.append(chr(n % 26 + ord('A')))
        n //= 26
    return ''.join(reversed(result))


def max_product_excel(words):
    n = len(words)
    masks = []
    lengths = []

    # Precompute masks and lengths
    for w in words:
        mask = 0
        for ch in set(w):  # use set to avoid duplicate letters
            mask |= 1 << (ord(ch) - ord('a'))
        masks.append(mask)
        lengths.append(len(w))

    max_product = 0
    for i in range(n):
        for j in range(i + 1, n):
            if masks[i] & masks[j] == 0:  # no common letters
                max_product = max(max_product, lengths[i] * lengths[j])

    return to_excel_column(max_product) if max_product > 0 else "0"


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    words = data[1:]
    print(max_product_excel(words))


if __name__ == "__main__":
    main()