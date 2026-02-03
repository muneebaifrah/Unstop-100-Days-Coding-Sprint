import sys

def calculate_golden_value(arr, n):
    MOD = 10**9 + 7 # Though not explicitly asked, use if numbers get huge
    
    # Prefix XOR array
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] ^ arr[i]
        
    total_se = 0
    total_so = 0
    
    # Process each bit independently (up to 31 bits for 10^9)
    for k in range(31):
        # count[parity][bit_value]
        # parity: 0 for even index, 1 for odd index
        # bit_value: 0 or 1 at the k-th bit of the prefix XOR
        count = [[0, 0], [0, 0]]
        
        bit_se = 0
        bit_so = 0
        
        for i in range(n + 1):
            p = i % 2
            v = (prefix[i] >> k) & 1
            
            # For current prefix[i], find how many previous prefix[j] 
            # have a different bit value (v^1).
            # If (i - j) is even, it contributes to SE.
            # If (i - j) is odd, it contributes to SO.
            
            # Same parity index (i%2 == j%2) -> i-j is Even
            bit_se += count[p][v ^ 1]
            
            # Different parity index (i%2 != j%2) -> i-j is Odd
            bit_so += count[1 - p][v ^ 1]
            
            # Update counts for next iterations
            count[p][v] += 1
            
        total_se += bit_se * (1 << k)
        total_so += bit_so * (1 << k)

    return abs(total_se - total_so)

def main():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))
    
    print(calculate_golden_value(arr, n))

if __name__ == "__main__":
    main()