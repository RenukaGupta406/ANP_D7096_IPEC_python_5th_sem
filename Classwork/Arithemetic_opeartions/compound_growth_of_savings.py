# Compound Growth of Savings Program

initial_amount = float(input("Enter the initial amount: "))
years = int(input("Enter the number of years: "))

final_amount = initial_amount * (2 ** years)

print("Final amount after", years, "years :", final_amount)