import time

print("Please insert your card")

time.sleep(5)

password = 1234
balance = 5500

pin = int(input("Enter your ATM pin: "))

if pin == password:
    while True:
        print("""
        1 == Check balance
        2 == Withdraw balance
        3 == Deposit balance
        4 == Exit
        """)
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue

        if option == 1:
            print(f"Your current balance is {balance}")
            print("==========================================================")
            print("==========================================================")
            print("==========================================================")
        elif option == 2:
           
            withdrawal_amount = int(input("Please enter withdraw amount: "))
           
            if withdrawal_amount > balance:
               
                print("Insufficient balance")
            else:
                
                balance = balance - withdrawal_amount
                
                print(f"{withdrawal_amount} is debited from your account")
                
                print(f"Your updated balance is {balance}")
                
                print("==========================================================")
                
                print("==========================================================")
                
                print("==========================================================")
        elif option == 3:
            
            deposit_amount = int(input("Please enter deposit amount: "))
            
            balance = balance + deposit_amount
            
            print(f"{deposit_amount} is credited to your account")
            
            print(f"Your updated balance is {balance}")
            
            print("==========================================================")
            
            print("==========================================================")
            
            print("==========================================================")
        elif option == 4:
            
            print("Thank you for using the ATM")
            
            break
        else:
            
            print("Invalid option, please try again")
else:
    
    print("You entered the wrong password")
