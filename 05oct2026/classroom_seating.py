total_students=int(input("enter number of students :"))
onebench=int(input("enter each bench hava :"))
total_bench=total_students//onebench
students_left=total_students%onebench
print(total_bench)
print(students_left)