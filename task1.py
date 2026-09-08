class BankAccount:
    def __init__(self, owner : str, balance : float, account_number : int):
        self.owner = owner
        self._balance = balance
        self.__account_number = account_number
    
    def owner_getter(self) -> str:
        return self.owner
    
    def owner_setter(self, newOwner) -> None:
        self.owner = newOwner
    def deposit(self, amound : float) -> None:
        self._balance += amound

bankAccount = BankAccount("zhandos", 500, 5)

print("old owner",bankAccount.owner_getter())

bankAccount.owner_setter("Nurlan")

print("new owner: ",bankAccount.owner_getter())
bankAccount.deposit(50)
print("new balance bankAccound",bankAccount._balance)


class SavingAccount(BankAccount):
    def deposit(self,amound : float, bonus : float):
        self._balance = self._balance + amound + bonus

savingAccount = SavingAccount("zhandos", 500, 5)

savingAccount.deposit(50,5)

print("new balance savingAccound",savingAccount._balance)

