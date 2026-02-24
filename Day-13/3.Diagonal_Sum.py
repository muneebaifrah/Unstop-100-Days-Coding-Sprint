def diagonal_sum(matrix, n):
    return 2 * n - 1 if n % 2 else 2 * n


if __name__ == '__main__':
    n = int(input())
    print(2 * n - 1 if n % 2 else 2 * n)