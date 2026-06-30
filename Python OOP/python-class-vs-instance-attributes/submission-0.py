class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    
    total_accounts = 0
    total_balance = 0

    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance

        BankAccount.total_accounts +=1
        BankAccount.total_balance+=balance

# TODO: Create two accounts
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 2000)

# TODO: Print the information using the mentioned format
print("Alice's balance: ${}".format(acc1.balance))
print("Bob's balance: ${}".format(acc2.balance))

print("Total Accounts: {}".format(acc1.total_accounts))
print("Total Balance: ${}".format(acc1.total_balance))

