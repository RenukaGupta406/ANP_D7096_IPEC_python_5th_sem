#Only vehicles having a valid parking pass are allowed to enter a private parking area. Accept either 1 (Valid Pass) or 0 (No Pass). • If the input is 1, display: Entry Allowed • Otherwise display: Entry Denied 
#parking entry validation
#input the parking number
num = int(input("Enetr the pass number (0 / 1) : "))
#validate the number
if (num < 0 and num>1):
    exit("wrong number.")
    print("-----------------------------------------")
#check the pass number
#if it is 1
if num==1:
    print("Entry Allowed ")
    print("-----------------------------------------")
#check the pass number
#if it is 0
if num==0:
    print("Entry Denied ")
    print("-----------------------------------------")