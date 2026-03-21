def minSwapsCouples(arr):
    n = len(arr)
    pos = {arr[i]: i for i in range(n)}
    swaps = 0
    
    for i in range(0, n, 2):
        first = arr[i]
        partner = first ^ 1
        
        if arr[i + 1] != partner:
            partner_index = pos[partner]
            
            # Update positions in map
            pos[arr[i + 1]] = partner_index
            arr[partner_index] = arr[i + 1]
            
            arr[i + 1] = partner
            pos[partner] = i + 1
            
            swaps += 1
    
    return swaps

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = minSwapsCouples(arr)
    print(result)