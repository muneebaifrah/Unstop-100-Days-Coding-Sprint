def can_select_people(N, K, arr):
    dp = [False] * (K + 1)
    dp[0] = True  # Sum 0 is always possible (select no elements)

    for num in arr:
        # Traverse backward to avoid using the same number multiple times
        for j in range(K, num - 1, -1):
            if dp[j - num]:
                dp[j] = True

    return "YES" if dp[K] else "NO"



def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # First input is the number of people
    K = int(data[1])  # Second input is the village number
    arr = list(map(int, data[2:2 + N]))  # Next N inputs are the numbers assigned to each person
    
    # Call user logic function and print the output
    result = can_select_people(N, K, arr)
    print(result)

if __name__ == "__main__":
    main()