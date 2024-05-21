principle = int(input("enter the principle amount:"))
interest_rate = int(input("enter your interest rate:"))
month = int(input("enter your month:"))
for i in range(month):
    interest_amount = principle*interest_rate/100
    #   0 = 50000*5/100
    #   2500 = 52500*5/100
    #   2625 = 55125*5/100
    #   2756 = 57881*5/100
    principle = principle + interest_amount
    #   0 = 50000 + 2500
    #   52500 = 52500 + 2625
    #   55125 = 55125 + 2756
    #   57881
print(principle)
