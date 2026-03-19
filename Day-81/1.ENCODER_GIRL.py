# User-defined function to be implemented
def processWords(n, s, x):
    # User needs to write the logic here
    a=[]
    l=s.split(' ')
    for i in range(len(l)):
      l[i]=l[i].replace(x,"")
    for j in l:
        a.append(len(j)) 
    a.sort()
    return a


if __name__ == "__main__":
    n = int(input())
    s = input().strip()
    x = input().strip()
    result = processWords(n, s, x)
    print(" ".join(map(str, result)))