t=int(input())
for _ in range(t):
    n=str(input())
    two=len(n)
    one=0
    if(int(n)%21==0):
        print("The streak is broken!")
    elif "21" in n:
        print("The streak is broken!")
    else:
        for i,j in enumerate(n):
            if j=="2" and i<two:
                two=i
            if j=="1" and i>one:
                one=i
        if(one>two):
            print("The streak is broken!")
        else:
            print("The streak lives still in our heart!")
