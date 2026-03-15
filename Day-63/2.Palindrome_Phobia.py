import sys
sys.setrecursionlimit(10000)

MOD = 10**9 + 7

def solve(N, S):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(pos, last, second_last, is_greater):
        if pos == N:
            return 1 if is_greater else 0

        total = 0
        start_char = ord('a')
        end_char = ord('z')

        # Determine the range of characters to try
        for c in range(start_char, end_char + 1):
            ch = chr(c)

            # Check palindrome constraints
            if ch == last:
                continue  # avoid "aa", "bb", etc.
            if ch == second_last:
                continue  # avoid "aba", "cdc", etc.

            # Lexicographical comparison
            if not is_greater:
                # We're still equal so far; need to match S[pos] or go above
                if ch < S[pos]:
                    continue
                elif ch == S[pos]:
                    total += dp(pos + 1, ch, last, False)
                else:
                    total += dp(pos + 1, ch, last, True)
            else:
                # Already greater, free to choose
                total += dp(pos + 1, ch, last, True)

            total %= MOD

        return total

    return dp(0, '', '', False)

# Input Handling
if __name__ == "__main__":
    N = int(input().strip())
    S = input().strip()
    print(solve(N, S))