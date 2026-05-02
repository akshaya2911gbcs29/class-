class InvalidPINError(Exception):
    pass
class AccountBlockedError(Exception):
    pass
class InsufficientBalance(Exception):
    pass
class ATM:
    def __init__(self):
        self.correct_pin = input("Set PIN: ")
        self.balance = float(input("Set balance: "))
        self.attempts = 0
        self.is_blocked = False
    def verify_pin(self, entered_pin):
        try:
            if self.is_blocked or self.attempts >= 3:
                self.is_blocked = True
                raise AccountBlockedError("Account blocked after 3 attempts")
            if entered_pin != self.correct_pin:
                self.attempts += 1
                raise InvalidPINError(f"Incorrect PIN. Attempts: {self.attempts}")
            print("PIN verified successfully")
            self.attempts = 0
            return True
        except InvalidPINError as e:
            print(e)
            if self.attempts >= 3:
                self.is_blocked = True
                print("Account blocked after 3 attempts")
            return False
        except AccountBlockedError as e:
            print(e)
            return False
    def withdraw(self, amount):
        try:
            if self.is_blocked or self.attempts >= 3:
                raise AccountBlockedError("Account blocked after 3 attempts")
            if amount > self.balance:
                raise InsufficientBalance("Insufficient balance")
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Remaining balance:", self.balance)
        except AccountBlockedError as e:
            print(e)
        except InsufficientBalance as e:
            print(e)
atm = ATM()
for i in range(4):
    pin = input("\nEnter PIN to withdraw: ")
    if atm.verify_pin(pin):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(withdraw_amount)
        break
    if atm.is_blocked:
        print("Your account is blocked .")
        break

