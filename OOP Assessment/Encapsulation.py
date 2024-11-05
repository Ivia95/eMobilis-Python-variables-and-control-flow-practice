class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid or insufficient funds")

    def get_balance(self):
        return self.__balance

# Demonstrate depositing and withdrawing money
account = BankAccount()

# Deposit money
account.deposit(100)
print(f"Balance after deposit: {account.get_balance()}")

# Withdraw money
account.withdraw(50)
print(f"Balance after withdrawal: {account.get_balance()}")

# Trying to access the private attribute directly (should fail)
# print(account.__balance)  # Uncommenting this line will raise an AttributeError

# Accessing balance through the getter method
print(f"Final balance: {account.get_balance()}")
