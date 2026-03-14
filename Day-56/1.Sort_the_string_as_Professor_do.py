def solve(order, s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    ans = []

    # first add characters present in custom order
    for ch in order:
        if ch in freq:
            ans.append(ch * freq[ch])
            del freq[ch]

    # remaining characters in alphabetical order
    for ch in sorted(freq.keys()):
        ans.append(ch * freq[ch])

    return "".join(ans)


def main():
    order, s = input().split()
    print(solve(order, s))


if __name__ == "__main__":
    main()