
class DailyLimitExceeded(Exception):
    pass

# Function to withdraw money with daily limit
def withdraw_from_atm(amount_today, amount_now):
    DAILY_LIMIT = 10000
    if amount_today + amount_now > DAILY_LIMIT:
        raise DailyLimitExceeded("You can't withdraw more than ₹10,000 in a day.")
    else:
        amount_today += amount_now
        print("Withdrawal successful. Total withdrawn today:", amount_today)


try:
    withdraw_from_atm(8000, 3000)  # 8000 already done, trying 3000 more = 11,000
except DailyLimitExceeded as e:
    print("Error:", e)
