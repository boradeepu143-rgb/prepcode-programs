try:
    a=input("enter number 1:")
    b=input("enter number 2:")
    print(int(a)/int(b))
except ValueError:
    print("give the number as a input")
except zeroDivisionError:
    print("cannot division by zero")