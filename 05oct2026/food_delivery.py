price=int(input("enter price :"))
quantity=int(input("enter quality :"))
delivery_charge=int(input("enter delivery charge :"))
discount=int(input("enter discount :"))
total_bill=price*quantity-(price*quantity*discount/100)+delivery_charge
print(total_bill)