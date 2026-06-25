principal = float(input("Enter principal amount :"))
if principal<0:
    exit("principal amount cannot be negaive")
rate = float(input("Enter annual interest rate(%) :"))
if rate<0:
    exit("rate of interest cannot be negative")
time = float(input("Enter time (years) :"))
if time<0:
    exit("Time cannot be negative")
amount = principal*(1 + rate/100) ** time
compound_interest = amount-principal
print("Compound Interest =" ,round(compound_interest,2))
print("Total Amount =" , round(amount,2))

