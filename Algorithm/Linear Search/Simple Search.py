n=int(input())
l=[int(i) for i in input().split()]
k=int(input())
for i,j in enumerate(l):
    if(j==k):
        print(i)