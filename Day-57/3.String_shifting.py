def shift_string(s, shifts):
    ans = []

    for i in range(len(s)):
        old_pos = ord(s[i]) - ord('a')
        new_pos = (old_pos + shifts[i]) % 26
        ans.append(chr(new_pos + ord('a')))

    return "".join(ans)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    s = data[1]
    shifts = list(map(int, data[2:2+n]))

    result = shift_string(s, shifts)
    print(result)


if __name__ == "__main__":
    main()