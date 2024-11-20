class bankaccount:
    def __init__(self,account_number,account_balance):
        self.__account_number=account_number
        self.__account_balance=account_balance
    
    def balance(self):
        return self.__account_balance
    
    def money_deposit(self,amount):
       if amount > 0:
           self.__account_balance += amount
       else:
           print("Invalid fund")

    def money_withdraw(self,amount):
        if 0<amount<=self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Out of fund or invalid fund")

bank_account = bankaccount("23A6789901",68000)
print(bank_account.balance())


bank_account.money_deposit(7200)
print(bank_account.balance())

bank_account.money_withdraw(1456)
print(bank_account.balance())
