n=int(input())
fat=list(map(int,input().split()))
protein=list(map(int,input().split()))
vitamin=list(map(int,input().split()))
l=[]
c=0
for num in fat:
    if num not in protein and num not in vitamin:
        c+=1
l.append(c)
c=0
for num in protein:
    if num not in fat and num not in vitamin:
        c+=1
l.append(c)
c=0
for num in vitamin:
    if num not in fat and num not in protein:
        c+=1
l.append(c)
print(*l)