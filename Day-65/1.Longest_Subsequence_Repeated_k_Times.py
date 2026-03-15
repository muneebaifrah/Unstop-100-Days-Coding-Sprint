from collections import deque, Counter

def longest_subsequence_repeated_k(s, k):
    freq = Counter(s)

    # characters that can appear in answer
    chars = [c for c in freq if freq[c] >= k]
    chars.sort(reverse=True)

    def valid(seq):
        target = seq * k
        i = 0
        for c in s:
            if i < len(target) and c == target[i]:
                i += 1
        return i == len(target)

    q = deque([""])
    ans = ""

    while q:
        cur = q.popleft()

        for c in chars:
            nxt = cur + c

            if valid(nxt):
                if len(nxt) > len(ans) or (len(nxt) == len(ans) and nxt > ans):
                    ans = nxt
                q.append(nxt)

    return ans


if __name__ == "__main__":
    s = input().strip()
    k = int(input())
    print(longest_subsequence_repeated_k(s, k))