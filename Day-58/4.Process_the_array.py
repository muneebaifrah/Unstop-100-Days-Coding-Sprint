def process_array(arr):
    n = len(arr)
    
    # Step 1: max, min, 2nd max, 2nd min...
    i, j = 0, n - 1
    temp = []
    
    while i <= j:
        if i != j:
            temp.append(arr[j])
            temp.append(arr[i])
        else:
            temp.append(arr[i])
        i += 1
        j -= 1
    
    # Step 2: left rotate by n//2
    s = n // 2
    result = temp[s:] + temp[:s]
    
    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    
    result = process_array(arr)
    print(*result)


if __name__ == "__main__":
    main()