from collections import deque

def min_operations(N, K):
    target_len = N
    start = K
    
    # If already has N digits
    if len(str(start)) >= target_len:
        return 0
    
    visited = set()
    q = deque([(start, 0)])  # (number, steps)
    visited.add(start)
    
    while q:
        num, steps = q.popleft()
        digits = set(int(d) for d in str(num))
        
        for d in digits:
            if d <= 1:  # multiplying by 0 or 1 is useless
                continue
            new_num = num * d
            if new_num not in visited:
                if len(str(new_num)) >= target_len:
                    return steps + 1
                visited.add(new_num)
                q.append((new_num, steps + 1))
    
    return -1


# Driver code
if __name__ == "__main__":
    N, K = map(int, input().split())
    print(min_operations(N, K))