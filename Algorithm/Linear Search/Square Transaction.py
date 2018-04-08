n=int(input())
l=[int(i) for i in input().split()]
c=0
m=int(input())
q=[int(i) for i in input().split()]
for t in q:
    s=0
    for i,j in enumerate(l):
        s=s+j
        if t<=s and c==0:
            c=1
            print(i,t)
    if c==1:
        print("-1")
        c=0