import sys
import math
from functools import reduce

def compute_gcd_of_list(arr):
    return reduce(math.gcd, arr)

def is_bad_group(soldiers):
    soldiers.sort()  # Sorting is mentioned but not essential for GCD
    return compute_gcd_of_list(soldiers) == 1

# Input handling
def main():
    n = int(input())
    soldiers = list(map(int, input().strip().split()))
    
    if is_bad_group(soldiers):
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    main()