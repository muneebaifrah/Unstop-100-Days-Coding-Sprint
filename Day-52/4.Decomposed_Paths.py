def user_logic(n, edges):
    import sys
    sys.setrecursionlimit(1_000_000)

    g = [[] for _ in range(n)]
    for a, b in edges:
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    # Check if feasible for given K
    def feasible(K: int) -> bool:
        dp = [1] * n   # dp[v]
        t = [1] * n    # t[v]: 1 if v is an endpoint of its color-path, else 0

        parent = [-1] * n
        order = []
        stack = [0]
        parent[0] = 0
        while stack:
            v = stack.pop()
            order.append(v)
            for to in g[v]:
                if to == parent[v]:
                    continue
                parent[to] = v
                stack.append(to)

        ok = True

        # helper: take top2 from small list
        def top2(vals):
            vals = [x for x in vals if x is not None]
            vals.sort(reverse=True)
            if not vals:
                return 0, 0
            if len(vals) == 1:
                return vals[0], 0
            return vals[0], vals[1]

        for v in reversed(order):
            # collect children contributions split by t[child]
            # endpoint-children: candidates to connect through v
            end1 = end2 = end3 = -10**18
            non1 = non2 = -10**18
            cnt_end = 0

            child_exists = False
            for to in g[v]:
                if to == parent[v]:
                    continue
                child_exists = True
                if t[to] == 1:
                    cnt_end += 1
                    x = dp[to]
                    if x > end1:
                        end3 = end2
                        end2 = end1
                        end1 = x
                    elif x > end2:
                        end3 = end2
                        end2 = x
                    elif x > end3:
                        end3 = x
                else:
                    x = dp[to]
                    if x > non1:
                        non2 = non1
                        non1 = x
                    elif x > non2:
                        non2 = x

            if not child_exists:
                dp[v] = 1
                t[v] = 1
                continue

            # CASE 1: <=1 endpoint-child
            if cnt_end <= 1:
                # endpoint child (if exists) contributes dp-1 (we can merge color upward)
                e_adj = (end1 - 1) if cnt_end == 1 else None

                m1, m2 = top2([
                    non1 if non1 > -10**17 else None,
                    non2 if non2 > -10**17 else None,
                    e_adj
                ])

                # constraints for paths through v
                if m1 + 1 > K:
                    return False
                if m2 > 0 and m1 + m2 + 1 > K:
                    return False

                t[v] = 1
                dp[v] = m1 + 1
                continue

            # CASE 2: >=2 endpoint-children
            # Scenario A: make v an endpoint (connect with the best endpoint-child -> decrement only end1)
            valsA = [
                non1 if non1 > -10**17 else None,
                non2 if non2 > -10**17 else None,
                (end1 - 1),        # connected one
                end2,              # unchanged
                end3               # unchanged
            ]
            a1, a2 = top2(valsA)
            cand = 10**18
            if a1 + 1 <= K and (a2 == 0 or a1 + a2 + 1 <= K):
                cand = a1 + 1

            # Scenario B: make v NOT an endpoint (connect with two best endpoint-children -> decrement end1 & end2)
            valsB = [
                non1 if non1 > -10**17 else None,
                non2 if non2 > -10**17 else None,
                (end1 - 1),
                (end2 - 1),
                end3
            ]
            b1, b2 = top2(valsB)

            # Scenario B must be feasible at least as an option; if not, fail
            if b1 + 1 > K:
                return False
            if b2 > 0 and b1 + b2 + 1 > K:
                return False

            dpB = b1 + 1  # dp if t[v]=0

            # choose better (smaller dp is better)
            if dpB < cand:
                t[v] = 0
                dp[v] = dpB
            else:
                t[v] = 1
                dp[v] = cand

        return ok

    # Binary search minimal K in [1..n]
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def main():
    import sys
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    edges = []
    for i in range(1, 2*(n-1)+1, 2):
        edges.append((int(data[i]), int(data[i+1])))
    print(user_logic(n, edges))

if __name__ == "__main__":
    main()