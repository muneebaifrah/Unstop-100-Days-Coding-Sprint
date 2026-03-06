def rearrange_blocks_to_form_name(S, P):
    n = len(S)
    m = len(P)

    if m > n:
        return 0, []

    p_count = [0]*26
    window = [0]*26

    for ch in P:
        p_count[ord(ch)-97] += 1

    result = []

    for i in range(n):
        window[ord(S[i])-97] += 1

        if i >= m:
            window[ord(S[i-m])-97] -= 1

        if window == p_count:
            result.append(i-m+2)  # 1-based index

    return len(result), result


if __name__ == "__main__":
    S = input().strip()
    P = input().strip()

    count, indices = rearrange_blocks_to_form_name(S, P)

    if count == 0:
        print("none")
    else:
        print(count)
        print(*indices)