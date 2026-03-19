import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0
    
    # Read N and Q
    N = int(data[idx])
    Q = int(data[idx + 1])
    idx += 2
    
    # Read the array
    arr = list(map(int, data[idx:idx + N]))
    idx += N

    # Precompute prefix sums
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + arr[i]
    
    # Process each query
    results = []
    for _ in range(Q):
        l = int(data[idx])
        m = int(data[idx + 1])
        r = int(data[idx + 2])
        idx += 3
        
        sum1 = prefix[m] - prefix[l]
        sum2 = prefix[r + 1] - prefix[m + 1]
        
        product = sum1 * sum2
        results.append(str(product if product >= 0 else 0))
    
    print("\n".join(results))

# Run the main function
main()