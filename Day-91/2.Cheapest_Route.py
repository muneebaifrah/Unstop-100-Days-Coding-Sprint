import heapq

def cheapest_route_with_discount(n, m, edges):
    graph = [[] for _ in range(n + 1)]

    for a, b, c in edges:
        graph[a].append((b, c))

    INF = 10**18
    dist = [[INF] * 2 for _ in range(n + 1)]
    dist[1][0] = 0

    pq = [(0, 1, 0)]  # (cost, node, coupon_used)

    while pq:
        cost, node, used = heapq.heappop(pq)

        if cost > dist[node][used]:
            continue

        for nxt, price in graph[node]:

            # Normal move (no coupon)
            if dist[nxt][used] > cost + price:
                dist[nxt][used] = cost + price
                heapq.heappush(pq, (dist[nxt][used], nxt, used))

            # Use coupon if not used yet
            if used == 0:
                discounted = price // 2
                if dist[nxt][1] > cost + discounted:
                    dist[nxt][1] = cost + discounted
                    heapq.heappush(pq, (dist[nxt][1], nxt, 1))

    return min(dist[n][0], dist[n][1])


# ---------- Input Handling ----------
if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    print(cheapest_route_with_discount(n, m, edges))