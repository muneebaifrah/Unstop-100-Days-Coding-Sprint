import sys

def user_logic(n, arr):
    if n < 2:
        return -1
    
    min_val = arr[0]
    max_diff = -1
    
    for i in range(1, n):
        if arr[i] > min_val:
            max_diff = max(max_diff, arr[i] - min_val)
        else:
            min_val = arr[i]
    
    return max_diff

def main():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    
    outputs = []
    
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        
        arr = list(map(int, input_data[index:index+n]))
        index += n
        
        result = user_logic(n, arr)
        outputs.append(str(result))
    
    print("\n".join(outputs))

if __name__ == "__main__":
    main()
