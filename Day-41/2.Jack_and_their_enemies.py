import math

def user_logic(n, enemy_groups, m):
    # Binary Search for the minimum kill rate K
    low = 1
    high = max(enemy_groups)
    ans = -1
    
    # If it's impossible (though constraints suggest N <= M), handle gracefully
    if n > m:
        return None

    while low <= high:
        mid = (low + high) // 2
        
        # Calculate total minutes needed with rate 'mid'
        total_time = 0
        for group in enemy_groups:
            # Equivalent to math.ceil(group / mid)
            total_time += (group + mid - 1) // mid
            
        if total_time <= m:
            ans = mid
            high = mid - 1  # Try to find a smaller K
        else:
            low = mid + 1   # Need to increase the kill rate
            
    if ans == -1:
        return None
    
    # Convert ans to octal string without the '0o' prefix
    octal_k = oct(ans)[2:]
    return ans, octal_k

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    enemy_groups = list(map(int, input_data[1:n+1]))
    m = int(input_data[n+1])
    
    result = user_logic(n, enemy_groups, m)
    
    if result:
        k, octal_k = result
        print(f"{k} {octal_k}")
    else:
        print(1)

if __name__ == "__main__":
    main()