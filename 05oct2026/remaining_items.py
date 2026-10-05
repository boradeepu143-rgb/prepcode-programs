total_product=int(input("enter products :"))
one_box=int(input("enter each box hava :"))
total_boxes=total_product//one_box
remaining_product=total_boxes%one_box
print("total_boxes :",total_boxes)
print("remaning_product :",remaining_product)