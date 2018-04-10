n=str(input())
l=[0]
count=0
for i in range(len(n)-1,-1,-1):
    if(int(n[i])%2==0):
        count+=1
        l.append(count)
    else:
        l.append(count)
l=l[::-1]
l.pop()
print(*l)