n=int(input())
s=""
for i in range(n):
    k=int(input())
    s+=str(k)
if int(s)%2==0:
    print(1)
else:
    print(0)