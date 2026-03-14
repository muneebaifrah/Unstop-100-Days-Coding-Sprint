def find_smallest_unexpressible_power(arr):
    arr.sort()
    
    reach = 1
    
    for x in arr:
        if x > reach:
            return reach
        reach += x
    
    return reach


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    result = find_smallest_unexpressible_power(arr)
    print(result)


if __name__ == "__main__":
    main()