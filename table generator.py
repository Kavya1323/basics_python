print("Multiplication table")
while True:
    n=int(input("enter a number"))
    if(n==0):
        print("thankyou")
        break;
    else:
        for i in range(0,11):
            print(f"{n} * {i} = {n*i}")