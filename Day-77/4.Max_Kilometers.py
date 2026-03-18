def solve(A, B, C, D):
    """
    Write your logic here.
    Parameters:
        A (int): Initial litres of petrol
        B (int): Total kilometers to travel
        C (int): Litres of petrol consumed per kilometer on petrol mode
        D (int): Litres of petrol consumed per kilometer on hybrid mode
    Returns:
        int: Maximum number of kilometers traveled using only petrol or -1 if not possible
    """
    if B*C <= A:
        return B
    elif B*D < A:
        return (B - (B*C - A)//(C-D) - 1) 
    return -1  
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    A = int(data[0])
    B = int(data[1])
    C = int(data[2])
    D = int(data[3])
    
    # Call user logic function and print the output
    result = solve(A, B, C, D)
    print(result)

if __name__ == "__main__":
    main()