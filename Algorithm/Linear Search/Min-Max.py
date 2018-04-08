n=int(input())
l=[int(i) for i in input().split()]
min=sum(l)
max=l[0]
for i in range(len(l)):
    a=l[:i]
    b=l[i+1:]
    c=a+b
    if(min>sum(c)):
        min=sum(c)
    if(max<sum(c)):
        max=sum(c)
print(min,max)