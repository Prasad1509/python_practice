num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
try:
    result=num1/num2
    print("Result:",result)
except ZeroDivisionError:
    print("Error: cannot didide by zero.")

except ValueError:
    print("Error: Invalid input . please enter integers only")
    12
