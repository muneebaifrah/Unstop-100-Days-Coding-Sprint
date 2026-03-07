def user_logic(l, r):
    mid = (r + 1) // 2
    
    if l > mid:
        return r % l
    else:
        return mid - 1


t = int(input().strip())

for _ in range(t):
    l, r = map(int, input().split())
    print(user_logic(l, r))