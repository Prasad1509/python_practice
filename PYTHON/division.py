num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num2==0:
    print("Error: Division by zero is not allowed.")
else:
    div=num1/num2
    print(f"Division:{num1}/{num2}={div}")