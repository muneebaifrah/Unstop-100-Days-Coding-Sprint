def diff_max_min(num: int) -> int:
    # Convert to string, handle sign
    sign = -1 if num < 0 else 1
    digits = list(str(abs(num)))

    if sign == 1:
        # Positive number
        max_val = int(''.join(sorted(digits, reverse=True)))
        min_val = int(''.join(sorted(digits)))
    else:
        # Negative number: max is least negative (digits sorted ascending)
        max_val = -int(''.join(sorted(digits)))
        min_val = -int(''.join(sorted(digits, reverse=True)))

    return max_val - min_val

# Driver code
T = int(input())
for _ in range(T):
    n = int(input())
    print(diff_max_min(n))