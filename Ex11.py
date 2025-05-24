class AgeRestrictionError(Exception):
    pass

def book_ticket(age):
    if age < 18:
        raise AgeRestrictionError("You must be at least 18 to watch this movie.")
    else:
        print("Ticket booked! Enjoy your movie.")

try:
    age = int(input("Enter your age to book a movie ticket: "))
    book_ticket(age)
except AgeRestrictionError as e:
    print("Booking failed:", e)
