from math import gcd
from collections import defaultdict

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def ksubarrays(a, n, k):
    subvec = set()
    
    for i in range(n - k + 1):
        contain_prime = False
        nums = []
        
        # Check if there is a prime in the current window
        for j in range(i, i + k):
            if is_prime(a[j]):
                contain_prime = True
                
        for j in range(i, i + k):
            if contain_prime or is_prime(a[j]):
                nums.append(a[j])
                contain_prime = True
                continue
            
            if len(nums) == 0:
                nums.append(a[j])
            else:
                if nums[-1] == 1 and a[j] == 1:
                    continue
                if gcd(nums[-1], a[j]) == 1:
                    nums.append(a[j])
                    
        if len(nums) == k:
            nums.sort()  # Sort the numbers for consistent output
            subvec.add(tuple(nums))  # Add a tuple to make it hashable
            
    return sorted(subvec)  # Sort the set to ensure consistent output order

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if k > n:
        print(0)
        return
    
    subvec = ksubarrays(a, n, k)
    for nums in subvec:
        print(' '.join(map(str, nums)))

if __name__ == "__main__":
    main()