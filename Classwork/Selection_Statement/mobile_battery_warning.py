#A smartphone displays a low battery warning only when the battery percentage falls below 15%. Write a Python program to accept the battery percentage. If the battery is below 15, display: Connect Charger Immediately Otherwise, display nothing. 
#mobile battery warning
#input the mobile battery
battery = int(input("Enter battery percentage(in %) : "))
#validate the battery percentage
if battery <0:
    exit("Battery cannot be negative.")
    print("------------------------------------------------------")
#check the battery percentage
#if it is less than or equal to 15%
if (battery <=15):
    print("Connect Charger Immediately ")
    print("------------------------------------------------------")


