def user_logic(n, seat_preferences):
    occupied = [False] * n
    result = [0] * n

    for i in range(n):
        pos = seat_preferences[i] - 1
        while occupied[pos]:
            pos = (pos + 1) % n
        occupied[pos] = True
        result[i] = pos + 1

    return result


def main():
    import sys
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    seat_preferences = list(map(int, data[1:]))

    final_seating = user_logic(n, seat_preferences)
    print(" ".join(map(str, final_seating)))


if __name__ == "__main__":
    main()