def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    
    result = []
    for num in arr:
        if not result or result[-1] != num:
            result.append(num)
    
    print(*result)

if __name__ == "__main__":
    main()