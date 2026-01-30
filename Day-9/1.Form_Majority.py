n = int(input().strip())
votes = list(map(int, input().split()))

total_sum = sum(votes)
votes.sort(reverse=True)

chosen = []
chosen_sum = 0

for v in votes:
    chosen.append(v)
    chosen_sum += v
    if chosen_sum > total_sum - chosen_sum:
        break

print(*chosen)
