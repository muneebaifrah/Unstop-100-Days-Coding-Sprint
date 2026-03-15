def find_largest_number(arr):
    # Write your logic here
    s=sorted(arr)
    a,b=s[0:2]
    a=str(a)
    b=str(b)
    c=int(a+b)
    b=int(b+a)
    return max(b,c)

    # Placeholder return value

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = find_largest_number(arr)
    print(result)