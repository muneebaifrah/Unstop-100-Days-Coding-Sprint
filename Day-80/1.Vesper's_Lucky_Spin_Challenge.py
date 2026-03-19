def solve():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N, X, P = map(int, input().split())
        target = (N - X) % N  # This is what (sum) % N must equal for new position to be 0

        found = False
        # We'll keep track of the sum mod N to detect cycles (optional optimization)
        visited = set()
        
        # sum_f = F*(F+1)//2
        for F in range(1, P + 1):
            sum_f = F * (F + 1) // 2
            if sum_f % N == target:
                print("Yes")
                found = True
                break

            # Optional: detect cycles to break early
            # mod_val = sum_f % N
            # if mod_val in visited:
            #     break
            # visited.add(mod_val)

        if not found:
            print("No")

if __name__ == "__main__":
    solve()