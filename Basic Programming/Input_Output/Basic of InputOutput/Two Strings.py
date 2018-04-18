n=int(input())
for _ in range(n):
    s=str(input())
    s=s.split(" ")
    c=0
    for i in s[0]:
        if i in s[1]:
            s[1].replace(i,"")
        else:
            c=1
            print("No")
            break
    if c==0:
        print("Yes")



