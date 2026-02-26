import math
n=int(input())
m=0
for i in range(n):
    t=math.pow(2,i)
    if t<=n:
        if t>m:
            m=t
    if t>n:
        break
print(int(m))
               