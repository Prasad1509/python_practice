class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter the positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative number not allowed!")
    print("You Entered:", num)

except NegativeNumberError as e:
    print("Error:", e)
except ValueError:
    print("Invalid input! Please enter an integer.")

