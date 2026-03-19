import bisect
def user_logic(n, arr, q, queries):
    """
    Write your logic here.
    Parameters:
        n (int): Number of elements in the array
        arr (list): List of integers representing the array
        q (int): Number of queries
        queries (list): List of integers representing the queries
    Returns:
        list: List of integers representing the results for each query
    """
    """for i in queries:
        for j in arr:
            if i==j or arr[i]>=j:
                d=arr[j]-queries[i]
            return arr[j]"""
    arr.sort()
    result = []
    for x in queries:
        idx = bisect.bisect_left(arr, x)
        if idx < n:
            result.append(arr[idx])
        else:
            result.append(-1)
    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        
        q = int(data[index])
        index += 1
        queries = list(map(int, data[index:index + q]))
        index += q
        
        # Call user logic function
        result = user_logic(n, arr, q, queries)
        results.extend(result)
    
    # Print all results for each query in each test case
    for res in results:
        print(res)


if __name__ == "__main__":
    main()