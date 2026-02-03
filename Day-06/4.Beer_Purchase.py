import sys

def main():
    input = sys.stdin.read().split()
    n = int(input[0])
    x = int(input[1])
    a = list(map(int, input[2:2+n]))
    a.sort()
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + a[i]
    
    total = 0
    prev_days = 0
    
    for k in range(n, 0, -1):
        sum_a = prefix[k]
        current_sum = sum_a + k * prev_days
        if current_sum > x:
            continue
        available = x - current_sum
        if available < 0:
            continue
        d_max = available // k
        m = d_max + 1
        total += k * m
        prev_days += m
    
    print(total)

if __name__ == "__main__":
    main()
                