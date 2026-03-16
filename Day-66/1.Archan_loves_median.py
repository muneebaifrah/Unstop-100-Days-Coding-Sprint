import sys
import heapq

left = []   # max heap (store negatives)
right = []  # min heap

k = int(sys.stdin.readline())

for _ in range(k):
    parts = sys.stdin.readline().split()

    if parts[0] == "add":
        v = int(parts[1])

        heapq.heappush(left, -v)
        heapq.heappush(right, -heapq.heappop(left))

        if len(right) > len(left):
            heapq.heappush(left, -heapq.heappop(right))

    else:  # get
        if len(left) > len(right):
            median = float(-left[0])
        else:
            median = (-left[0] + right[0]) / 2

        print(f"{median:.1f}")