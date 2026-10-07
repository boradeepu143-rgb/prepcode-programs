cinema_charge=int(input("enter actual movie charge :"))
age=int(input("enter age :"))
if age<12:
    ticket_price=cinema_charge*0.50
elif age>=60:
    ticket_price=cinema_charge*0.70
else:
    ticket_price=cinema_charge
print(f"ticket price is :₹{cinema_charge}")