def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        s = data[index]
        index += 1
        
        unique_sub = set()
        
        for i in range(len(s) - 1):
            unique_sub.add(s[i:i+2])
        
        results.append(str(len(unique_sub)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()