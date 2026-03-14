def calculate_difference(arr):
    positive = sorted(set(x for x in arr if x > 0))
    
    if not positive:
        return -1
    
    max_power = max(positive)
    
    best_len = 0
    best_last = 0
    
    start = positive[0]
    prev = positive[0]
    
    for i in range(1, len(positive)):
        if positive[i] == prev + 1:
            prev = positive[i]
        else:
            length = prev - start + 1
            if length > best_len:
                best_len = length
                best_last = prev
            elif length == best_len:
                best_last = min(best_last, prev)
            
            start = positive[i]
            prev = positive[i]
    
    length = prev - start + 1
    if length > best_len:
        best_len = length
        best_last = prev
    elif length == best_len:
        best_last = min(best_last, prev)
    
    return abs((best_last + 1) - max_power)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    
    result = calculate_difference(arr)
    print(result)


if __name__ == "__main__":
    main()