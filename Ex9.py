
class InsufficientFunds(Exception):
    pass


def withdraw_money(balance, amount):
    if amount > balance:
        raise InsufficientFunds("You don't have enough money in your account.")
    else:
        balance -= amount
        print("Withdrawal successful. Remaining balance:", balance)

try:
    withdraw_money(500, 70)  # Only have 500, trying to withdraw 700
except InsufficientFunds as e:
    print("Error:", e)
