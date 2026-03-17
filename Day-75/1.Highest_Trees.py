from collections import deque

def sliding_window_maximum(arr, N, K):
    dq = deque()
    result = []

    for i in range(N):
        # Remove elements smaller than the current element from the deque's back
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()

        # Add current element index to the deque
        dq.append(i)

        # Remove the element if it is out of the current window
        if dq[0] == i - K:
            dq.popleft()

        # Start adding max to result once first full window is processed
        if i >= K - 1:
            result.append(arr[dq[0]])

    return result

def main():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    res = sliding_window_maximum(arr, N, K)
    print(*res)

if __name__ == "__main__":
    main()