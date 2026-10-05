total_units=int(input("enter number of consumed unit :"))
group=int(input("enter a no of groups :"))
complete_units=total_units//group
remaining=total_units%group
print(" complete group ",complete_units)
print("remaining",remaining)