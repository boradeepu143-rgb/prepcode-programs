student_percentage=int(input("enter student prcentage:"))
student_attendence=int(input("enter student attendence :"))
if student_percentage<=85 and student_attendence>=75:
    print("sudent recieves scholarship")
else:
    print("not eligible for scholarship")