def find_good_numbers(n):
    good_numbers = []
    for num in range(n + 1):
        s = str(num)
        if len(s) == 1:
            good_numbers.append(num)
            continue
        good = True
        for i in range(1, len(s)):
            if abs(int(s[i]) - int(s[i - 1])) != 1:
                good = False
                break
        if good:
            good_numbers.append(num)
    return good_numbers

    pass


def main():
    import sys
    input = sys.stdin.read
    data = input().strip()

    n = int(data)  # First input is the integer n

    # Call user logic function and print the output
    result = find_good_numbers(n)

    # Print the result in the required format
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()