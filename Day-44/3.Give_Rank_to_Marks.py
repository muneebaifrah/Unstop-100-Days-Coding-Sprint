def assignRanks(N, marks):
    sorted_marks = sorted(set(marks), reverse=True)  # Unique and sorted in descending order
    rank_map = {mark: rank+1 for rank, mark in enumerate(sorted_marks)}  # Map marks to rank
    return [rank_map[mark] for mark in marks]  # Assign ranks back to original order

# Input handling
N = int(input().strip())
marks = list(map(int, input().split()))
print(*assignRanks(N, marks))