def pudding(n):
    if n[len(n)-1]=='0':
        return 0
    return 1
    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    T = int(data[0])  # First input is the integer T
    results = []
    
    for i in range(1, T + 1):
        n = data[i]
        result = pudding(n)
        results.append(result)
    
    for result in results:
        print(1 if result else 0)

if __name__ == "__main__":
    main()