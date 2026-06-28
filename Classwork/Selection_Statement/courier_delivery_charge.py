#A courier company calculates delivery charges based on the package weight. • Weight up to 2 kg → ₹50  • Weight greater than 2 kg and up to 5 kg → ₹100  • Weight greater than 5 kg → ₹180
#delivery charge calculator
weight = float(input("enter the weight : "))
#validete the weight
print("---------------------------------------------------")
if (weight<0):
    exit("weight cannot be negative.")

#check the weight to 2kg
#if it less than or equal to 2kg
if (weight <= 2):
    print("Delivery Charge = 50 rupees")
    print("----------------------------------------------------")
#check the weight to 2kg or 5kg
#if it is more then 2kg or less then equal to 5kg
elif (weight > 2 and weight <= 5):
    print("Delivery Charge = 100 rupees")
    print("-----------------------------------------------------")
#otherwise 
else :
    print("Delivery Charge =180 rupees")
    print("-----------------------------------------------------")
    