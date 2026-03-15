def count_distinct_positions(T, test_cases):
    results = []
    for N, X, S in test_cases:
        visited = set()
        position = X
        visited.add(position)

        for move in S:
            if move == 'L':
                position -= 1
            elif move == 'R':
                position += 1
            visited.add(position)

        results.append(len(visited))
    return results

# Input Handling
if __name__ == "__main__":
    T = int(input())
    test_cases = []

    for _ in range(T):
        while True:
            line = input().strip()
            if line:
                break
        N, X = map(int, line.split())
        S = input().strip()
        test_cases.append((N, X, S))

    results = count_distinct_positions(T, test_cases)
    for res in results:
        print(res)