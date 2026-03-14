def canFormStrings(s, arr):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for word in arr:
        temp = freq.copy()
        for ch in word:
            if temp.get(ch, 0) == 0:
                return False
            temp[ch] -= 1
    return True


if __name__ == '__main__':
    import sys

    data = sys.stdin.read().split()
    if not data:
        print("false")
    else:
        s = data[0]
        n = int(data[1])
        arr = data[2:2 + n]

        result = canFormStrings(s, arr)
        print('true' if result else 'false')