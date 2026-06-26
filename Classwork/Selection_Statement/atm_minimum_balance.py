# ============================================
# Program    : ATM Minimum Balance Check
# Description: Checks if account balance meets
#              the minimum balance requirement
# ============================================

# ---------- Constant Value ----------
# Minimum balance required by the bank
MINIMUM_BALANCE = 5000

# ---------- Taking Input from User ----------
balance = float(input("Enter Account Balance: "))

# ---------- Input Validation ----------
# Balance cannot be negative
if balance < 0:
    print("Invalid! Account balance cannot be negative.")

# ---------- Selection Statement - Balance Check ----------
elif balance < MINIMUM_BALANCE:
    # If balance is less than 5000 → Show Warning
    print("--------------------------------------------")
    print("Warning! Your account balance is below the  ")
    print("minimum required balance of ₹5000.          ")
    print("--------------------------------------------")
    print("Your Current Balance  : ₹", balance)
    print("Minimum Balance Needed: ₹", MINIMUM_BALANCE)
    print("Shortfall Amount      : ₹", MINIMUM_BALANCE - balance)
    print("--------------------------------------------")

else:
    # If balance is 5000 or above → All Good
    print("--------------------------------------------")
    print("Your account balance meets the requirement. ")
    print("--------------------------------------------")
    print("Your Current Balance  : ₹", balance)
    print("Minimum Balance Needed: ₹", MINIMUM_BALANCE)
    print("Extra Balance         : ₹", balance - MINIMUM_BALANCE)
    print("--------------------------------------------")