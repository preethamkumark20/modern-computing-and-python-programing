n=int(input("enter the number:"))
if(n<0):
    print("please enter positive number")
else:
    i=1
    while(i!=11):
        print(f"{n}*{i}={n*i}")
        i=i+1