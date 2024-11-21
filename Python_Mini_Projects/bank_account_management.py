class Bankbalance:
    def __init__(self,account_number,account_holder_name,balance):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._balance = balance

    def view_balance(self):
        return  self._balance
    
    def deposit_money(self,amount):
        if amount > 0:
            self._balance += amount
            print("account balance after deposit:",self._balance)
        else:
            print("Invalid fund or Invalid amount")

    def withdraw_money(self,amount):
        if 0 < amount <=self._balance:
            self._balance -= amount
            print("account balance after withdraw:",self._balance)
        else:
            print("Insufficient amount or Invalid fund")

class Savingsaccount(Bankbalance):
    def __init__(self,account_number,account_holder_name,balance,interest):
        super().__init__(account_number,account_holder_name,balance)
        self._interest = interest

    def savings_account_details(self):
        print("Account holder name:",self._account_holder_name)
        print("Account Number:",self._account_number)
        print("Savings account Balance is:",self._balance)

    def Interest_rate(self,months):
        principle = self._balance
        for i in range(months):
            interest_amount = principle*self._interest/100
            principle +=interest_amount
        self._balance = principle
        print("Updated balance:",months,"months at the interest rate:",self._interest,"the balance is:",self._balance)

class Currentaccount(Bankbalance):
    def __init__(self,account_number,account_holder_name,balance,overdaft_limit):
        super().__init__(account_number,account_holder_name,balance)
        self._overdraft_limit = overdaft_limit

    def current_account_details(self):
        print("Account holder name:",self._account_holder_name)
        print("Account Number:",self._account_number)
        print("Savings account balance is:",self._balance)

    def overdraft_limit_money(self,amount):
        if 0 < amount <= self._balance + self._overdraft_limit :
            self._balance -= amount
            print("The money withdrew:",amount,"Including overdraft:",self._balance)
        else:
            print("Invalid money or Overdraft excluded")

savings_acc = Savingsaccount("A345100000781","Dwayne",450000,2.5)
savings_acc.savings_account_details()
savings_acc.Interest_rate(7)
savings_acc.deposit_money(24900)
savings_acc.view_balance()

current_acc = Currentaccount("A345100000781","Dwayne",28000,2500)
current_acc.current_account_details()
current_acc.overdraft_limit_money(1500)
current_acc.overdraft_limit_money(2500)
current_acc.deposit_money(5789)
current_acc.view_balance()



     