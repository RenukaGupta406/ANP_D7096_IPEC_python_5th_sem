#A digital vault can only be opened if the user enters the correct security code. Write a Python program that accepts the entered security code. If the entered code is 7890, display: "Access Granted to the Vault." Otherwise, do nothing. 
#secure vault access
#input the code
code = int(input("Enter the vault code : "))
print("----------------------------------------")
#validate the code
if code<=0:
    exit("Invalid! the code is not be negative.")
    print("-------------------------------------")
#check the code
#if it is matched
if code == 7890:
    print("Access granted to the vault.")
    print("--------------------------------------")
