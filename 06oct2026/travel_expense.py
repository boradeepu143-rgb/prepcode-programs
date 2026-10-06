person_travel=int(input("enter distance km :"))
liter_1=int(input("enter liter per :"))
per_litre=int(input("enter per liter kilometers :"))
total=person_travel//per_litre
fuel_expense=total*liter_1
print(fuel_expense)