import sys

def can_invite(k, n, friends):
    count = 0
    # We try to fill positions 0, 1, ..., k-1
    # For a person to be at position 'count', they need:
    # Richer: (k - 1 - count) <= Ai
    # Poorer: count <= Bi
    for ai, bi in friends:
        if count <= bi and (k - 1 - count) <= ai:
            count += 1
            if count == k:
                return True
    return False

def user_logic(n, friends):
    low = 1
    high = n
    ans = 1
    
    while low <= high:
        mid = (low + high) // 2
        if can_invite(mid, n, friends):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

def main():
    # Use fast I/O for large constraints (N=2*10^5)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    index = 0
    T_str = input_data[index]
    T = int(T_str)
    index += 1
    
    output = []
    for _ in range(T):
        n = int(input_data[index])
        index += 1
        friends = []
        for i in range(n):
            ai = int(input_data[index])
            bi = int(input_data[index + 1])
            friends.append((ai, bi))
            index += 2
        
        output.append(str(user_logic(n, friends)))
    
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    main()
                
