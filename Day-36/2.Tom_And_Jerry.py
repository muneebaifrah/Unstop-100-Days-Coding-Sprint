import heapq

def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    k = int(data[1])
    nums = list(map(int, data[2:]))

    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    print(heap[0])

if __name__ == "__main__":
    main()