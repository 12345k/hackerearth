n=int(input())
l=[]
for _ in range(n):
    s=str(input()).split()
    for i in s:
        if(i.isdigit()):
            l.append(i)
for i in set(l):
    for _ in range(n):
        s
