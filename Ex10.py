
class InvalidAccountNumber(Exception):
    pass


def check_account(account_number):
    valid_accounts = ["1111", "2222", "3333"]
    if account_number not in valid_accounts:
        raise InvalidAccountNumber("This account number doesn't exist.")
    else:
        print("Account found. You can proceed.")


try:
    check_account("1111")
except InvalidAccountNumber as e:
    print("Error:", e)
