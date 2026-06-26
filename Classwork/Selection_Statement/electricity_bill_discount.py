# ============================================
# Program    : Electricity Bill Discount
# Description: Applies 10% discount if bill
#              is ₹5000 or more
# ============================================

# ---------- Constant Values ----------
DISCOUNT_PERCENTAGE = 10      # 10% discount
MINIMUM_BILL_FOR_DISCOUNT = 5000  # Minimum bill to get discount

# ---------- Taking Input from User ----------
bill_amount = float(input("Enter the electricity bill amount: "))

# ---------- Input Validation ----------
# Bill amount cannot be negative or zero
if bill_amount < 0:
    print("Invalid! Bill amount cannot be negative.")

elif bill_amount == 0:
    print("Invalid! Bill amount cannot be zero.")

# ---------- Selection Statement - Discount Check ----------
elif bill_amount >= MINIMUM_BILL_FOR_DISCOUNT:
    # If bill is ₹5000 or more → Apply 10% Discount

    discount_amount = (DISCOUNT_PERCENTAGE / 100) * bill_amount
    final_amount    = bill_amount - discount_amount

    print("--------------------------------------------")
    print("Discount Applied!                           ")
    print("--------------------------------------------")
    print("Original Bill Amount : ₹", bill_amount)
    print("Discount Percentage  :", DISCOUNT_PERCENTAGE, "%")
    print("Discount Amount      : ₹", discount_amount)
    print("Final Bill Amount    : ₹", final_amount)
    print("--------------------------------------------")
    print("You Saved            : ₹", discount_amount)
    print("--------------------------------------------")

else:
    # If bill is less than ₹5000 → No Discount

    print("--------------------------------------------")
    print("No Discount Applied!                        ")
    print("--------------------------------------------")
    print("Your Bill Amount     : ₹", bill_amount)
    print("Final Bill Amount    : ₹", bill_amount)
    print("--------------------------------------------")
    print("Tip: Bills above ₹5000 get 10% discount!   ")
    print("--------------------------------------------")