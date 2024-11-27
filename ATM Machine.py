print("*"*20,"ATM Machine","*"*20)
amount = int(input("Enter the amount"))
l = [500,200,100,50,20,10,5,2,1]
c = 0
for i in l:
    Notes = amount//i 
    c = c + Notes
    print(f"{i} notes --> {Notes}")
    # amount = amount - i*Notes
    amount = amount%i
print("Minimum number of Notes:",c)