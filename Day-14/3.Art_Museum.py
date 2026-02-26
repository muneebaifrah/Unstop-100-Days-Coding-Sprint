def user_logic(n, positions):
    xs = []
    ys = []
    
    for x, y in positions:
        xs.append(x)
        ys.append(y)
    
    xs.sort()
    ys.sort()
    
    # Count optimal x positions
    if n % 2 == 1:
        count_x = 1
    else:
        count_x = xs[n // 2] - xs[n // 2 - 1] + 1
    
    # Count optimal y positions
    if n % 2 == 1:
        count_y = 1
    else:
        count_y = ys[n // 2] - ys[n // 2 - 1] + 1
    
    return count_x * count_y



def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    positions = []
    index = 1
    for i in range(n):
        x = int(data[index])
        y = int(data[index + 1])
        positions.append((x, y))
        index += 2
    
    # Call user logic function and print the output
    result = user_logic(n, positions)
    print(result)

if __name__ == "__main__":
    main()