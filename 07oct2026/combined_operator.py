price=int(input("enter product price:"))
quantity=int(input("enter quantity :"))
member=input("does customer hava valid coupon ?(yes/no) :").lower()=="yes"
coupon=input("does customer hava valid coupon?(yes/no) :").lower()=="yes"


MEMBER_DISCOUNT=0.10
COUPON_DISCOUNT=0.05
total_amount=price*quantity

if member:
    total_amount=total_amount*(1-MEMBER_DISCOUNT)
    if coupon:
        total_amount=total_amount*(1-COUPON_DISCOUNT)
        print(f"final payable amount :${total_amount :.2f}")
