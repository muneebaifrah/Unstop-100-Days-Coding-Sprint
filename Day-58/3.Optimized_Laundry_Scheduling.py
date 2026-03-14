import heapq

def user_logic(K, N, M, W, D):
    wash_heap = []
    for t in W:
        heapq.heappush(wash_heap, (t, t))   # (finish_time, machine_time)

    wash_times = []
    for _ in range(K):
        finish, machine = heapq.heappop(wash_heap)
        wash_times.append(finish)
        heapq.heappush(wash_heap, (finish + machine, machine))

    dry_heap = []
    for t in D:
        heapq.heappush(dry_heap, (t, t))    # (finish_time, machine_time)

    dry_times = []
    for _ in range(K):
        finish, machine = heapq.heappop(dry_heap)
        dry_times.append(finish)
        heapq.heappush(dry_heap, (finish + machine, machine))

    wash_times.sort()
    dry_times.sort(reverse=True)

    ans = 0
    for i in range(K):
        ans = max(ans, wash_times[i] + dry_times[i])

    return ans


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    K = int(data[0])
    N = int(data[1])
    M = int(data[2])

    W = list(map(int, data[3:3+N]))
    D = list(map(int, data[3+N:3+N+M]))

    print(user_logic(K, N, M, W, D))


if __name__ == "__main__":
    main()