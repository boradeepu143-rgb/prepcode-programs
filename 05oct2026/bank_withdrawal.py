amount=int(input("enter amount :"))
required_amount=int(input("enter required amount :"))
if amount>=required_amount and amount%500==0:
    print("allow withdrawal")
else:
    print("not allowed withdrawal")