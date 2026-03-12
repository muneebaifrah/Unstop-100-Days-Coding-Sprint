# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve(arr):
    ans = 0
    mx = 0

    for x in arr:
        ans += x

    for i in range(len(arr)):
        ans += (len(arr) - i) * max(arr[i] - mx, 0)
        mx = max(mx, arr[i])

    return ans

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve(arr)
    print(result)