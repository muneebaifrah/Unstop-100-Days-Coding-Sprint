def solve(nums):
    # User logic goes here.
    # Parameters:
    #  nums: List[int] - List of integers
    # Returns:
    #  int - Computed result based on the problem statement
    n = len(nums)
    ans = 0

    # Sliding window with bitmask
    mask = 0
    l = 0

    for r in range(n):
        # Shrink window until nums[r] can fit without conflict
        while (mask & nums[r]) != 0:
            mask ^= nums[l]
            l += 1
        mask |= nums[r]

        # Count only subarrays of length >= 2
        length = r - l + 1
        if length >= 2:
            ans += (length - 1)

    return ans


def main():
    import sys
    data = sys.stdin.read().strip().split()
    n = int(data[0])                # first token is N
    v = list(map(int, data[1:1+n])) # next N tokens are the array elements
    print(solve(v))


if __name__ == "__main__":
    main()

'''
if __name__ == "__main__":
    n = int(input())
    v = list(map(int, input().split()))
    print(solve(v))
'''