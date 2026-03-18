def count_strictly_increasing_substrings(S):
    N = len(S)
    unique_substrings = set()

    for i in range(N):
        current = S[i]
        unique_substrings.add(current)
        for j in range(i + 1, N):
            if S[j] > S[j - 1]:
                current += S[j]
                unique_substrings.add(current)
            else:
                break  # stop if the sequence is no longer strictly increasing

    return len(unique_substrings)

# Input handling
def main():
    N = int(input())
    S = input().strip()
    print(count_strictly_increasing_substrings(S))

if __name__ == "__main__":
    main()