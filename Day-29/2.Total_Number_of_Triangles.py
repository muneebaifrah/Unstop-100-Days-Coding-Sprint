def colored_cells(n):
    """
    Write your logic here.
    Parameters:
        n (int): Number of iterations
    Returns:
        int: Total number of triangles
    """
    if n == 0:
        return 0
    
    # Formula: 1 + 3 * (n-1) * n / 2
    # This can be rewritten as: 1 + 3n(n-1)/2
    # Or: (2 + 3n² - 3n) / 2
    # Or: (3n² - 3n + 2) / 2
    
    total = 1 + (3 * (n - 1) * n) // 2
    return total

def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    
    # Call user logic function and print the output
    result = colored_cells(n)
    print(result)

if __name__ == "__main__":
    main()