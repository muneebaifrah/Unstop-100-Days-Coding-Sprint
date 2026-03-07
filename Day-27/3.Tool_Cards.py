def user_logic(n, positions_cards):
    left = []
    right = []

    for p, c in positions_cards:
        if p < 0:
            left.append((abs(p), c))
        elif p > 0:
            right.append((p, c))

    left.sort()
    right.sort()

    left_cards = [c for _, c in left]
    right_cards = [c for _, c in right]

    L = len(left_cards)
    R = len(right_cards)

    k = min(L, R)

    total = sum(left_cards[:k]) + sum(right_cards[:k])

    if L > R:
        total += left_cards[k]
    elif R > L:
        total += right_cards[k]

    return total


n = int(input().strip())
positions_cards = [tuple(map(int, input().split())) for _ in range(n)]

print(user_logic(n, positions_cards))