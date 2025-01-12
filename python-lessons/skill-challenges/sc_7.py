import unittest

class BankAccount:
    def __init__(self, initial_balance: int | float = 0):
        self._balance = initial_balance

    def deposit(self, deposit_amount: int | float):
        if not deposit_amount > 0: 
            raise ValueError("You may only deposit amounts greater than $0.")
        self._balance += deposit_amount

    def withdraw(self, withdrawal_amount: int | float):
        if not withdrawal_amount > 0: 
            raise ValueError("You may only withdraw amounts greater than $0.")
        if withdrawal_amount > self._balance:
            raise ValueError("Not enough funds in account to make withdrawal.")
        
        self._balance -= withdrawal_amount

    @property
    def balance(self):
        return self._balance

    def __repr__(self):
        f"A {self.__class__} with ${self._balance} in it."

class Savings(BankAccount):
    def __init__(self, initial_balance: int | float = 0, interest_rate: float = 0.0035):
        super().__init__(initial_balance)
        self.interest_rate = interest_rate

    def pay_interest(self):
        self.deposit(self.balance * self.interest_rate)

class HighInterest(BankAccount):
    def __init__(self, initial_balance: int | float = 0, interest_rate: float = 0.007, withdrawal_fee: int | float = 5):
        super().__init__(initial_balance)
        self.interest_rate = interest_rate
        self._withdrawal_fee = withdrawal_fee

    def pay_interest(self):
        self.deposit(self.balance * self.interest_rate)

    def withdraw(self, withdrawal_amount):
        if not withdrawal_amount > 0: 
            raise ValueError("You may only withdraw amounts greater than $0.")
        if withdrawal_amount + self._withdrawal_fee > self._balance - 5:
            raise ValueError("Not enough funds in account to make withdrawal.")
        
        self._balance -= (withdrawal_amount + self._withdrawal_fee)

class LockedIn(BankAccount):
    def __init__(self, initial_balance: int | float = 0, interest_rate: float = 0.009):
        super().__init__(initial_balance)
        self.interest_rate = interest_rate

    def pay_interest(self):
        self.deposit(self.balance * self.interest_rate)

    def withdraw(self, withdrawal_amount):
        raise NotImplementedError("Withdrawals are not allowed for a LockedIn account.")

class TestBankAccounts(unittest.TestCase):
    def test_bank_account(self):
        account = BankAccount(100)
        self.assertEqual(account.balance, 100)
        account.deposit(50)
        self.assertEqual(account.balance, 150)
        account.withdraw(20)
        self.assertEqual(account.balance, 130)
        with self.assertRaises(ValueError):
            account.withdraw(200)
        with self.assertRaises(ValueError):
            account.deposit(-10)

    def test_savings(self):
        account = Savings(100)
        account.pay_interest()
        self.assertAlmostEqual(account.balance, 100.35)

    def test_high_interest(self):
        account = HighInterest(100)
        account.withdraw(10)
        self.assertEqual(account.balance, 85)  # 100 - 10 - 5 fee
        with self.assertRaises(ValueError):
            account.withdraw(90)
        account.pay_interest()
        self.assertAlmostEqual(account.balance, 85.595)

    def test_locked_in(self):
        account = LockedIn(100)
        account.pay_interest()
        self.assertAlmostEqual(account.balance, 100.9)
        with self.assertRaises(NotImplementedError):
            account.withdraw(10)

if __name__ == "__main__":
    unittest.main()
