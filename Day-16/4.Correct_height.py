def heightChecker(heights):
    expected = sorted(heights)
    count = 0
    
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1
            
    return count

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = heightChecker(arr)
    print(result)