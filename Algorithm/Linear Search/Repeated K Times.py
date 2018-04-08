n=int(input())
l=[int(i) for i in input().split()]
k=int(input())
m=[]
for i in set(l):
    if(l.count(i)==k):
        m.append(i)
print(min(m))
