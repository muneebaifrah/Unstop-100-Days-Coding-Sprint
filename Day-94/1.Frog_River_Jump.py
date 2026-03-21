def can_frog_cross_river(nums):
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= len(nums) - 1:
            return True
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    nums = list(map(int, data[1:n+1]))
    
    result = can_frog_cross_river(nums)
    print("true" if result else "false")

if __name__ == "__main__":
    main()