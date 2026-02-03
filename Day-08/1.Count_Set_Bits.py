def count_ones_in_binary(n):
    total = 0
    for i in range(1, n + 1):
        total += bin(i).count('1')
    return total


if __name__ == "__main__":
    n = int(input())
    result = count_ones_in_binary(n)
    print(result)
                     