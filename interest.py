principle = int(input("enter the principle amount:"))
interest_rate = int(input("enter your interest rate:"))
month = int(input("enter your month:"))
for i in range(month):
    interest_amount = principle*interest_rate/100
    principle = principle + interest_amount
print(principle)
