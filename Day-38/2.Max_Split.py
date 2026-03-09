def best_split_index(N, S):
    if N == 0:  # edge case
        return -1
    
    # Step 1: left distinct counts
    left = [0] * N
    seen_left = [False] * 10
    count = 0
    for i, ch in enumerate(S):
        d = int(ch)
        if not seen_left[d]:
            seen_left[d] = True
            count += 1
        left[i] = count

    # Step 2: right distinct counts
    right = [0] * N
    seen_right = [False] * 10
    count = 0
    for i in range(N-1, -1, -1):
        d = int(S[i])
        if not seen_right[d]:
            seen_right[d] = True
            count += 1
        right[i] = count

    # Step 3: find best split
    best_score = -1
    best_index = 0
    for i in range(N-1):  # split at i, right part starts at i+1
        score = left[i] + right[i+1]
        if score > best_score:
            best_score = score
            best_index = i
    
    return best_index


# Input handling
if __name__ == "__main__":
    N = int(input().strip())
    S = input().strip()
    print(best_split_index(N, S))
                