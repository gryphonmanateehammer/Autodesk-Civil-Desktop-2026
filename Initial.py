from dataclasses import dataclass


@dataclass
class Transaction:
    description: str
    category: str
    amount: float


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount: float, description: str):
        self.balance += amount
        self.transactions.append(
            Transaction(description, "Deposit", amount)
        )

    def withdraw(self, amount: float, description: str):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(
                Transaction(description, "Withdrawal", amount)
            )

    def print_statement(self):
        print("Bank Statement")
        print("==============")
        print(f"Account Owner: {self.owner}")
        print(f"Balance: ${self.balance:.2f}")
        print("--------------")

        for transaction in self.transactions:
            print(
                f"{transaction.description} | "
                f"{transaction.category} | "
                f"${transaction.amount:.2f}"
            )


account = BankAccount("Alex", 1500.00)

account.deposit(750.00, "Monthly Salary")
account.withdraw(120.50, "Groceries")
account.withdraw(80.00, "Transport")
account.deposit(250.00, "Freelance Payment")
account.withdraw(45.99, "Subscription")

account.print_statement()