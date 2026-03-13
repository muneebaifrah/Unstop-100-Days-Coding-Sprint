MOD = 10**9 + 7

def user_logic(n, heights):
    # Build pattern between consecutive labels i and i+1 in terms of positions pos[i]
    # '<' means pos[i] < pos[i+1]
    # '>' means pos[i] > pos[i+1]
    # '?' means no constraint (equal heights)
    pat = []
    for i in range(n - 1):
        if heights[i] > heights[i + 1]:
            pat.append('<')
        elif heights[i] < heights[i + 1]:
            pat.append('>')
        else:
            pat.append('?')

    # DP:
    # dp[j] = number of valid ways for labels 1..i (current i),
    #         where pos[i] is the (j+1)-th smallest among the used positions.
    dp = [1]  # i = 1

    for i in range(2, n + 1):
        sign = pat[i - 2]  # relation between (i-1) and i in pos[]
        total = sum(dp) % MOD

        if sign == '?':
            # no constraint between pos[i-1] and pos[i]
            dp = [total] * i
            continue

        # prefix sums of dp (length i-1)
        pref = [0] * (i - 1)
        run = 0
        for idx, val in enumerate(dp):
            run += val
            if run >= MOD:
                run -= MOD
            pref[idx] = run

        new = [0] * i
        if sign == '<':
            # pos[i-1] < pos[i]  => previous rank t < new rank j
            # new[j] = sum_{t=0..j-1} dp[t]
            for j in range(1, i):
                new[j] = pref[j - 1]
            # new[0] stays 0
        else:
            # sign == '>'
            # pos[i-1] > pos[i] => previous rank t >= new rank j
            # new[j] = sum_{t=j..i-2} dp[t] = total - sum_{t=0..j-1}
            for j in range(i):
                if j == 0:
                    new[j] = pref[-1]
                else:
                    new[j] = (pref[-1] - pref[j - 1]) % MOD

        dp = new

    return sum(dp) % MOD


def main():
    import sys
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    heights = list(map(int, data[1:1 + n]))
    print(user_logic(n, heights))


if __name__ == "__main__":
    main()