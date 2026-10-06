bankamount=int(input("enter amount:"))
customer_deposite=int(input("enter value :"))
withdrawal=int(input("enter value:"))
total_amount=customer_deposite+bankamount
balance=total_amount-withdrawal
print(balance)