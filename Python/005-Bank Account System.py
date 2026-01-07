import random
import datetime

accounts = {}

def generate_account_number():
    return "ACC" + str(random.randint(1000,9999))

def get_current_date():
    return datetime.date.today().strftime("%Y-%m-%d")

def create_account():
    account_number = generate_account_number()
    name = input("Enter Your Name : ")
    
    deposit_loop = True
    while deposit_loop:
        deposit = float(input("Inital Deposit : "))
        if deposit < 0:
            print("You Can Not Deposit Wrong Amount Of Money")
        else:
            break
    
    pin_loop = True
    while pin_loop:
        pin = input("Enter Your Pin (4 Digits Only) : ")
        if len(pin) == 4 and pin.isdigit():
            pin_loop = False
            break
        else:       
            print("Invalid Pin")

    account_type = input("Your Account Type (Savings/Current) : ")
    transaction_date = get_current_date()
    accounts[account_number]= {
        "name" : name,
        "balance" : deposit,
        "pin" : pin,
        "account_type" : account_type,
        "transactions" : []
    }

    return account_number

def deposit():
    acc_number = input("Enter Your Account Number : ")
    
    if acc_number not in accounts:
        return "Account Not Found"
    
    pin_attempt = input("Enter Pin : ")
    if pin_attempt != accounts[acc_number]["pin"]:
        return "Invalid Pin"
    
    amount_input = input("Enter Deposit Amount : ")

    is_valid_number = True
    decimal_count = 0
    has_digits = False

    for char in amount_input:
        if char == ".":
            decimal_count += 1
            if decimal_count >1:
                is_valid_number = False
                break
            elif char.isdigit():
                has_digits = True
            else:
                is_valid_number = False
                break
    
    if not is_valid_number or amount_input == "" or not has_digits:
        return "Invalid Amount. Enter Valid Amount."
    
    amount = float(amount_input)

    if amount <= 0:
        return "Amount Must Be Greater Than Zero (0)"
    
    accounts[acc_number]["balance"] += amount

    transaction_date = get_current_date()
    new_balance = accounts[acc_number]["balance"]
    transaction = (transaction_date,"Deposit",amount,new_balance)
    accounts[acc_number]["transactions"].append(transaction)

    return f"Deposit Successful! New Balance : {new_balance:,.2f}"

def withdraw():
    acc_number = input("Enter Account Number : ")

    if acc_number not in accounts:
        return "Account Not Found"

    attempts = 0
    while attempts < 3:
        pin_attempt = input("Enter Pin : ")
        if pin_attempt != accounts[acc_number]["pin"]:
            attempts += 1
            print(f"Invalid Pin! Try Again! {3-attempts} Left!")
        else:
            break
    
    if attempts == 3:
        return "Too many wrong PIN attempts! Transaction cancelled."
    
    amount_input = input("Enter Withdrawal Amount : ")

    is_valid_number = True
    decimal_count = 0
    has_digits = False

    for char in amount_input:
        if char == ".":
            decimal_count += 1
            if decimal_count >1:
                is_valid_number = False
                break
            elif char.isdigit():
                has_digits = True
            else:
                is_valid_number = False
                break
    
    if not is_valid_number or amount_input == "" or not has_digits:
        return "Invalid Amount. Enter Valid Amount."
    
    amount = float(amount_input)

    if amount <= 0:
        return "Amount Must Be Greater Than Zero (0)"
    elif amount > accounts[acc_number]["balance"]:
        return "Insufficient Amount For Withdrawal"
    
    accounts[acc_number]["balance"] -= amount

    transaction_date = get_current_date()
    new_balance = accounts[acc_number]["balance"]
    transaction = (transaction_date,"Withdraw",amount,new_balance)
    accounts[acc_number]["transactions"].append(transaction)

    return f"Withdrawal Successful! New Balance : {new_balance:,.2f}"

def check_balance():
    acc_number = input("Enter Account Number : ")

    if acc_number not in accounts:
        return "Account Not Found"

    attempts = 0
    while attempts < 3:
        pin_attempt = input("Enter Pin : ")
        if pin_attempt != accounts[acc_number]["pin"]:
            attempts += 1
            print(f"Invalid Pin! Try Again! {3-attempts} Left!")
        else:
            break
    
    if attempts == 3:
        return "Too many wrong PIN attempts! Transaction cancelled."

    bank_balance = accounts[acc_number]["balance"]

    return f"Your Current Balance : {bank_balance:,.2f}"

def transfer():
    sender_acc_number = input("Enter Sender's Account Number : ")

    if sender_acc_number not in accounts:
        return "Account Not Found"

    attempts = 0
    while attempts < 3:
        pin_attempt = input("Enter Pin : ")
        if pin_attempt != accounts[sender_acc_number]["pin"]:
            attempts += 1
            print(f"Invalid Pin! Try Again! {3-attempts} Left!")
        else:
            break
    
    if attempts == 3:
        return "Too many wrong PIN attempts! Transaction cancelled."
    
    receiver_acc_number = input("Enter Receiver's Account Number : ")

    if receiver_acc_number not in accounts:
        return "Account Not Found"
    elif receiver_acc_number == sender_acc_number:
        return "Same Account Can't Be Selected Transfer The Money"

    amount_input = input("Enter Transfer Amount : ")

    is_valid_number = True
    decimal_count = 0
    has_digits = False

    for char in amount_input:
        if char == ".":
            decimal_count += 1
            if decimal_count >1:
                is_valid_number = False
                break
            elif char.isdigit():
                has_digits = True
            else:
                is_valid_number = False
                break
    
    if not is_valid_number or amount_input == "" or not has_digits:
        return "Invalid Amount. Enter Valid Amount."
    
    amount = float(amount_input)

    if amount <= 0:
        return "Amount Should Be Greater Than Zero. Enter Valid Amount."
    elif amount > accounts[sender_acc_number]["balance"]:
        return "Amount Is More Than Your Balance. Enter Valid Amount."

    accounts[sender_acc_number]["balance"] -= amount
    accounts[receiver_acc_number]["balance"] += amount


    transaction_date = get_current_date()
    sender_new_balance = accounts[sender_acc_number]["balance"]
    receiver_new_balance = accounts[receiver_acc_number]["balance"]
    sender_transaction = (transaction_date,f"Transfer To {receiver_acc_number}",-amount,sender_new_balance)
    receiver_transaction = (transaction_date,f"Transfer From {sender_acc_number}",amount,receiver_new_balance)

    accounts[sender_acc_number]["transactions"].append(sender_transaction)
    accounts[receiver_acc_number]["transactions"].append(receiver_transaction)

    return f"Your Transfer Successful. Your New Balance {sender_new_balance:,.2f}"

def account_statement():
    acc_number = input("Enter Account Number : ")

    if acc_number not in accounts:
        return "Account Not Found"

    attempts = 0
    while attempts < 3:
        pin_attempt = input("Enter Pin : ")
        if pin_attempt != accounts[acc_number]["pin"]:
            attempts += 1
            print(f"Invalid Pin! Try Again! {3-attempts} Left!")
        else:
            break
    
    if attempts == 3:
        return "Too many wrong PIN attempts! Transaction cancelled."
    
    if "transactions" not in accounts[acc_number]:
        accounts[acc_number]["transactions"] = []

    print("\n" + "="*40)
    print("        ACCOUNT STATEMENT")
    print("="*40)
    print(f"Account: {acc_number}")
    print(f"Name: {accounts[acc_number]['name']}")
    print(f"Account Type: {accounts[acc_number]['account_type']}")
    print("="*40)
    print(f"{'Date':<12} {'Type':<15} {'Amount':>12} {'Balance':>12}")
    print("-"*55)
    
    transactions = accounts[acc_number]["transactions"]
    
    if transactions:
        for transaction in transactions:
            date = transaction[0]
            trans_type = transaction[1]
            amount = transaction[2]
            balance = transaction[3]
            
            amount_str = f"${amount:,.2f}"
            balance_str = f"${balance:,.2f}"
            
            print(f"{date:<12} {trans_type:<15} {amount_str:>12} {balance_str:>12}")
        
        print("-"*55)
        print(f"Total Transactions: {len(transactions)}")
        print(f"Current Balance: ${accounts[acc_number]['balance']:,.2f}")
    else:
        print("No transactions found.")
        print(f"Current Balance: ${accounts[acc_number]['balance']:,.2f}")
    
    print("="*40)
    
    return "Account Statement Generated Successfully"

def main_menu():
    """Simple and clean banking system menu"""
    print("\n" + "★"*50)
    print("       WELCOME TO PYTHON BANKING SYSTEM")
    print("★"*50)
    
    while True:
        print("\n" + "="*50)
        print("            BANKING MENU")
        print("="*50)
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Account Statement")
        print("7. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            acc_num = create_account()
            print(f"\n✅ Account created successfully!")
            print(f"   Account Number: {acc_num}")
            print("   Keep your account number safe!")
            
        elif choice == "2":
            result = deposit()
            print(f"\n{result}")
            
        elif choice == "3":
            result = withdraw()
            print(f"\n{result}")
            
        elif choice == "4":
            result = check_balance()
            print(f"\n{result}")
            
        elif choice == "5":
            result = transfer()
            print(f"\n{result}")
            
        elif choice == "6":
            result = account_statement()
            print(f"\n{result}")
            
        elif choice == "7":
            print("\n" + "="*50)
            print("  Thank you for using our Banking System!")
            print("            See you next time! 👋")
            print("="*50)
            break
            
        else:
            print("\n❌ Invalid choice! Please enter 1-7")
        
        if choice != "7":
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
