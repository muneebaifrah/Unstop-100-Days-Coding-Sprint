s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print("false")
else:
    a = sorted(s1)
    b = sorted(s2)
    if all(a[i] >= b[i] for i in range(len(a))) or all(b[i] >= a[i] for i in range(len(a))):
        print("true")
    else:
        print("false")