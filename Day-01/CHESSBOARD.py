import sys

s = input()
a = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

col = a[s[0]]
row = int(s[1])

if (col + row) % 2 == 0:
    print("Black")
else:
    print("White")