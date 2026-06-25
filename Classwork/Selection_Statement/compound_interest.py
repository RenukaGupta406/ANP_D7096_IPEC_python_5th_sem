principal = float(input("Enter principal amount :"))
if principal<0:
    print("principal amount cannot be negaive")
rate = float(input("Enter annual interest rate(%) :"))
if rate<0:
    print("rate of interest cannot be negative")
time = float(input("Enter time (years) :"))
if time<0:
    print("Time cannot be negative")
amount = principal*(1 + rate/100) ** time
compound_interest = amount-principal
print("Compound Interest =" ,round(compound_interest,2))
print("Total Amount =" , round(amount,2))

