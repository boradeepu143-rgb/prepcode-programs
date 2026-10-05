num1=int(input("enter number 1 :"))
num2=int(input("enter number 2 :"))
operator=input("enter operator (+,-,*,/) :")
if operator=='+':
   result=num1+num2
elif operator=='-':
     result=num1-num2
elif operator=='*':
     result=num*num2
elif operator=='/':
    result=num1/num2
else:
    print("invalid operator")
print(result)