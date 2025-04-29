class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"💸 Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")
        else:
            print("❌ Withdrawal failed. Check balance or amount.")

    def display_balance(self):
        print(f"💰 {self.owner}'s account balance: ₹{self.balance}")


# Sample usage
account = BankAccount("Alice", 1000)
account.display_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)  # Invalid withdrawal
