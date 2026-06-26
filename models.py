from typing import Self


class FinancialCalculatorMixin:
    def __init__(self):
        self.accounts: list[BankAccount] = []

    @property
    def money(self) -> int:
        summ = 0
        for account in self.accounts:
            summ += account.balance
        return summ

    def __eq__(self, other: Self):
        return self.money == other.money

    def __ge__(self, other: Self):
        return self.money >= other.money

    def __gt__(self, other: Self):
        return self.money > other.money


class Person(FinancialCalculatorMixin):
    def __init__(self, name: str):
        super().__init__()
        self.name = name.strip().title()

    def __str__(self) -> str:
        return f"Person {self.name}"


class BankAccount:
    def __init__(self, owner: Person, bank: 'Bank'):
        self.owner = owner
        self.bank = bank
        self.balance = 0

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        self.balance -= amount

    def transfer_money(self, other: Self, amount: int):
        self.balance -= amount
        other.balance += amount
        print(f'Money was transferred {amount} ({self} -> {other})')


    def __str__(self) -> str:
        return f'<Account was opened in {self.bank.title} for {self.owner.name}: current balance {self.balance}>'

    __repr__ = __str__


class Bank(FinancialCalculatorMixin):
    def __init__(self, title: str):
        super().__init__()
        self.title = f"PAT {title.strip().upper()}"

    def __str__(self) -> str:
        return f"Bank '{self.title}'"

    def open_account(self, client: Person) -> BankAccount:
        bank_account = BankAccount(owner=client, bank=self)
        self.accounts.append(bank_account)
        client.accounts.append(bank_account)
        return bank_account
