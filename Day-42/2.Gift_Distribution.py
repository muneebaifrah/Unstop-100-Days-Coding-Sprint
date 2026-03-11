import sys

def solve():
    # Read n from standard input
    line = sys.stdin.read().strip()
    if not line:
        return
    n = int(line)

    # Calculate total sum of 1 to n
    total_sum = n * (n + 1) // 2

    # If the total sum is odd, we cannot split it into two equal integer sums
    if total_sum % 2 != 0:
        print("NO")
        return

    print("YES")
    set1 = []
    set2 = []
    
    target = total_sum // 2
    
    # Greedy approach from largest to smallest works for this specific problem
    for i in range(n, 0, -1):
        if i <= target:
            set1.append(i)
            target -= i
        else:
            set2.append(i)

    # Output for Set 1
    print(len(set1))
    print(*(set1))
    
    # Output for Set 2
    print(len(set2))
    print(*(set2))

if __name__ == "__main__":
    solve()
                