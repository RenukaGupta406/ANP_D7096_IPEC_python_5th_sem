# ============================================
# Program  : Student Grade Calculator
# Description : Accepts marks and displays grade
# ============================================

# ---------- Taking Input from User ----------
marks = float(input("Enter Marks: "))

# ---------- Input Validation ----------
# Marks must be between 0 and 100
if marks < 0:
    print("Invalid! Marks cannot be negative.")

elif marks > 100:
    print("Invalid! Marks cannot be greater than 100.")

# ---------- Grade Calculation using Selection Statements ----------
# If marks are valid, calculate the grade

elif marks >= 90 and marks <= 100:
    # Marks between 90 to 100 → Grade A (Excellent)
    print("-----------------------------")
    print("Marks Entered :", marks)
    print("Grade         : A")
    print("Remark        : Excellent!")
    print("-----------------------------")

elif marks >= 75 and marks <= 89:
    # Marks between 75 to 89 → Grade B (Good)
    print("-----------------------------")
    print("Marks Entered :", marks)
    print("Grade         : B")
    print("Remark        : Good!")
    print("-----------------------------")

elif marks >= 50 and marks <= 74:
    # Marks between 50 to 74 → Grade C (Average)
    print("-----------------------------")
    print("Marks Entered :", marks)
    print("Grade         : C")
    print("Remark        : Average!")
    print("-----------------------------")

else:
    # Marks below 50 → Grade F (Fail)
    print("-----------------------------")
    print("Marks Entered :", marks)
    print("Grade         : F")
    print("Remark        : Failed! Work Harder.")
    print("-----------------------------")