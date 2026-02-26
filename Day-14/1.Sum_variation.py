n=int(input())
a=input()
c=0
for char in a:
    if char=='U' or char=='R':
        c+=1
    elif char=='D' or char=='L':
        c-=1
if c==0:
    print("YES")
else:
    print("NO")