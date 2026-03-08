import bisect

def user_logic(n, arr, b):
    arr.sort()
    b.sort()
    
    interest1 = 0
    interest2 = 0
    
    for x in arr:
        interest1 += bisect.bisect_right(b, x)
    
    for x in b:
        interest2 += bisect.bisect_right(arr, x)
    
    return max(interest1, interest2)


n = int(input())
arr = list(map(int, input().split()))
b = list(map(int, input().split()))

print(user_logic(n, arr, b))
                