def compute_rank_changes(n, arr):
    first_occurrence = {}
    last_occurrence = {}

    for idx, student_id in enumerate(arr):
        pos = idx + 1  # converting to 1-based index
        if student_id not in first_occurrence:
            first_occurrence[student_id] = pos
        last_occurrence[student_id] = pos

    result = []
    for idx, student_id in enumerate(arr):
        change = last_occurrence[student_id] - first_occurrence[student_id]
        result.append(change)

    return result

# Input
n = int(input())
arr = list(map(int, input().split()))

# Process
result = compute_rank_changes(n, arr)

# Output
print(' '.join(map(str, result)))