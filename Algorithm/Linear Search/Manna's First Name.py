n=int(input())
for _  in range(n):
    s=str(input())
    full = str(s.count("SUVOJIT"))
    s=s.replace("SUVOJIT","")
    first =str(s.count("SUVO"))
    print("SUVO = "+first+", SUVOJIT = "+full)