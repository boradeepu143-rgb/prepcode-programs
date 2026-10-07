m1=int(input("enter a chemistry :"))
m2=int(input("enter physics :"))
m3=int(input("enter maths :"))
average=m1+m2+m3/3
print(average)
if (m1>=40) and (m2>=40) and (m3>=40):
    if average >=75:
       print("student recive disction")
else:
    print("not recived distriction")