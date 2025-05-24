# Custom exception
class ResultTooLargeError(Exception):
    pass

def divide_numbers(a, b):
    try:
        result = a / b
        if result > 100:
            raise ResultTooLargeError("The result is too large!")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ResultTooLargeError as e:
        print("Custom Error:", e)
    else:
        print("Division result:", result)
    finally:
        print("Operation completed.")

# Example usage
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    divide_numbers(x, y)
except ValueError:
    print("Please enter valid integers.")
