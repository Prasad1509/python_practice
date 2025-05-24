#Catching multiple exception  in one  except block using a tuple.
try:
    num1=int(input("Enter First Number:"))
    num2=int(input("Enter Second Number:"))

    result=num1/num2
    print("Result:",result)
except (ZeroDivisionError,ValueError):
    print("Error:Either you enterd invalid input or tried dividing by zero.")