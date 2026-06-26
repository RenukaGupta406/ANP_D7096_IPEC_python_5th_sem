# ============================================
# Program    : Shopping Mall Parking Fee Waiver
# Description: Waives parking fee if purchase
#              amount is ₹2000 or more,
#              otherwise charges ₹100
# ============================================

# ---------- Constant Values ----------
MINIMUM_PURCHASE   = 2000    # Minimum purchase for free parking
PARKING_FEE        = 100     # Parking fee if not waived
FREE_PARKING_FEE   = 0       # No fee if purchase meets minimum

# ---------- Taking Input from User ----------
purchase_amount = float(input("Enter the purchase amount: "))

# ---------- Input Validation ----------
# Purchase amount cannot be negative
if purchase_amount < 0:
    print("Invalid! Purchase amount cannot be negative.")

# ---------- Selection Statement - Parking Fee Check ----------
elif purchase_amount >= MINIMUM_PURCHASE:
    # If purchase is ₹2000 or more → Parking Fee Waived

    print("--------------------------------------------")
    print("Parking Fee Waived!                         ")
    print("--------------------------------------------")
    print("Purchase Amount  : ₹", purchase_amount)
    print("Minimum Required : ₹", MINIMUM_PURCHASE)
    print("Parking Fee      : ₹", FREE_PARKING_FEE)
    print("--------------------------------------------")
    print("Thank you for shopping with us!             ")
    print("--------------------------------------------")

else:
    # If purchase is less than ₹2000 → Pay Parking Fee

    print("--------------------------------------------")
    print("Parking Fee Applicable!                     ")
    print("--------------------------------------------")
    print("Purchase Amount  : ₹", purchase_amount)
    print("Minimum Required : ₹", MINIMUM_PURCHASE)
    print("Parking Fee      : ₹", PARKING_FEE)
    print("--------------------------------------------")
    shortfall = MINIMUM_PURCHASE - purchase_amount
    print("Shop for ₹", shortfall, "more to get free parking!")
    print("--------------------------------------------")