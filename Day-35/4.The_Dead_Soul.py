# Python 3
import math

def find_minimum_k(a, b, c):
    """
    Write your logic here.
    Parameters:
        a (int): Coefficient of x^2
        b (int): Coefficient of x
        c (int): Constant term
    Returns:
        int: Minimum possible integer value of |K|
    """
    # For the line y = kx to intersect parabola y = ax^2 + bx + c
    # We need: ax^2 + (b-k)x + c = 0 to have real solutions
    # Discriminant: (b-k)^2 - 4ac >= 0
    # (b-k)^2 >= 4ac
    
    discriminant_base = 4 * a * c
    
    # If 4ac <= 0, then (b-k)^2 >= 4ac is always true for any k
    # So k = 0 works
    if discriminant_base <= 0:
        return 0
    
    # sqrt(4ac)
    sqrt_val = math.sqrt(discriminant_base)
    
    # We need: |b - k| >= sqrt(4ac)
    # This means: b - k >= sqrt(4ac) OR b - k <= -sqrt(4ac)
    # Which gives: k <= b - sqrt(4ac) OR k >= b + sqrt(4ac)
    
    k_low = b - sqrt_val   # k <= k_low
    k_high = b + sqrt_val  # k >= k_high
    
    # Find the closest integer k in valid ranges
    # For k <= k_low: largest valid integer is floor(k_low)
    # For k >= k_high: smallest valid integer is ceil(k_high)
    
    k1 = math.floor(k_low)
    k2 = math.ceil(k_high)
    
    # Also check if 0 falls in valid range
    # If 0 <= k_low or 0 >= k_high, then k=0 is valid
    if 0 <= k_low or 0 >= k_high:
        return 0
    
    # Otherwise, find minimum |k| from k1 and k2
    return min(abs(k1), abs(k2))


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    T = int(data[0])  # First input is the number of test cases
    index = 1
    results = []
    
    for _ in range(T):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        index += 3
        
        # Call user logic function and store the result
        result = find_minimum_k(a, b, c)
        results.append(result)
    
    # Print all results for each test case
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
              