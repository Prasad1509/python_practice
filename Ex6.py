try:
    # Outer try block
    num1 = int(input("Enter a number: "))
    try:
        # Inner try block
        result = 10 / num1
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
