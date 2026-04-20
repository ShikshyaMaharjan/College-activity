class Bank:
    accounts = {}  # class variable: stores all accounts
    total_balance = 0

    @classmethod
    def open_account(cls, name, balance):
        cls.accounts[name] = balance
        cls.total_balance += balance
        print(f"Account opened for {name}")

    @classmethod
    def close_account(cls, name):
        if name in cls.accounts:
            cls.total_balance -= cls.accounts[name]
            del cls.accounts[name]
            print(f"Account closed for {name}")
        else:
            print("Account not found")

    @classmethod
    def display_accounts(cls):
        print("Accounts:", cls.accounts)
        print("Total Bank Balance:", cls.total_balance)
Bank.open_account("Ram", 1000)
Bank.open_account("Sita", 2000)
Bank.display_accounts()
Bank.close_account("Ram")
Bank.display_accounts()