password=input("enter password :")
valid=len(password)>=8 and any(not ch.isalnum()for ch in password)
print(valid)