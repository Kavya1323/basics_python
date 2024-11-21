name=input()
marks=int(input())
if(marks>=90):
    grade= "A grade"
elif(80<=marks<=89):
    grade="B grade"
elif(70<=marks<=79):
    grade="C grade"
elif(60<=marks<=69):
    grade="D garde"
else:
    grade="Fail"
print(grade)