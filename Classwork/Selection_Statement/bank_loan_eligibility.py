# ============================================
# Program    : Bank Loan Eligibility Check
# ============================================

# Minimum salary required for loan
MINIMUM_SALARY = 30000

# Taking Input from User
salary = float(input("Enter your monthly salary: "))

# Input Validation
if salary < 0:
    print("Invalid! Salary cannot be negative.")

elif salary == 0:
    print("Invalid! Salary cannot be zero.")

# Selection Statement - Loan Eligibility Check
elif salary >= MINIMUM_SALARY:
    print("Congratulations! You are eligible to apply for the loan.")

else:
    print("Sorry! You are not eligible to apply for the loan.")
    