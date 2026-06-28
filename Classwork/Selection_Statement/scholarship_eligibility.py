#A university provides a scholarship only to students who score 90 or above. Write a Python program to accept a student's percentage and determine whether the student is eligible. • If percentage is 90 or above, display: Scholarship Approved • Otherwise display: Scholarship Not Approved 
#scholarship eligibity
#input the marks in percentage
marks = float(input("Enter the marks of the student(in % ) :"))
#validate the marks
if marks < 0:
    exit("marks cannot be negative.")
    print("------------------------------------------------------")
#check the marks of the student
#if it is less than 90 %
if marks < 90:
    print("Scholarship not approved.")
    print("-------------------------------------------------------")
#otherwise print message
else:
    print("Scholarship approved.")
    print("------------------------------------------------------")
