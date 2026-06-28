#restaurant bill discount
#enter the input
bill = float(input("Enter the bill amount: ₹"))
if bill<0:
    exit("bill amount not be negative")

if bill < 1000:
    print("No Discount")
elif bill >= 1000 and bill <= 2999:
    discount = bill * 10 / 100
    final_bill = bill - discount
    print("10% Discount Applied")
    print(f"Discount Amount: ₹{discount}")
    print(f"Final Bill: ₹{final_bill}")
else:
    discount = bill * 20 / 100
    final_bill = bill - discount
    print("20% Discount Applied")
    print(f"Discount Amount: ₹{discount}")
    print(f"Final Bill: ₹{final_bill}")