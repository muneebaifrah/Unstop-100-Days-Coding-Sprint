import math

def another_permutation_problem(nums, K):
    N = len(nums)
    
    # If K is >= N, we can cover the whole array in 1 operation
    if K >= N:
        return 1
    
    # We use 1 operation to cover the first K elements.
    # The remaining (N - K) elements must be covered.
    # Each additional operation can cover at most (K - 1) new elements
    # because it must overlap with at least one 'max' element already created.
    
    remaining_elements = N - K
    additional_ops = math.ceil(remaining_elements / (K - 1))
    
    return 1 + additional_ops

def main():
    import sys
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    n = int(input_data[0])
    # The problem asks for nums[1] = nums[N], which means 
    # making the whole array the same value (the max).
    nums = list(map(int, input_data[1:n+1]))
    K = int(input_data[n+1])
    
    result = another_permutation_problem(nums, K)
    print(result)

if __name__ == "__main__":
    main()
                