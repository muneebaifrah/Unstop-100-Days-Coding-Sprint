def highestAltitude(n, arr):
    curr_alt = 0
    max_alt = 0

    for gain in arr:
        curr_alt = curr_alt + gain

        if curr_alt > max_alt:
            max_alt = curr_alt

    return max_alt

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = highestAltitude(n, arr)
    print(result)