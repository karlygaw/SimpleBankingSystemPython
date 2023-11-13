# Simple Banking System for QSTEM

# Хранение данных для аккаунтов
accounts = []

def create_new_acc(): #
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter your initial deposit amount: "))
    
    account_number = float(input())
    account = {"name": name, "account_number": account_number, "balance": initial_deposit, "history": []}
    
    accounts.append(account)
    
    print(f"Account created successfully. Your account number is {account_number}.")

def deposit():
    account_number = int(input("Enter your account number: "))
    account = find_account(account_number)
    
    if account:
        deposit_amount = float(input("Enter the deposit amount: "))
        account["balance"] += deposit_amount
        account["history"].append(f"Deposited {deposit_amount} tenge.")
        print(f"Deposit successful. Your new balance is {account['balance']}.")
    else:
        print("Invalid account number. Please try again.")

def withdraw_funds():
    account_number = int(input("Enter your account number: "))
    account = find_account(account_number)
    
    if account:
        withdrawal_amount = float(input("Enter the withdrawal amount: "))
        if withdrawal_amount <= account["balance"]:
            account["balance"] -= withdrawal_amount
            account["history"].append(f"Withdrew {withdrawal_amount} tenge.")
            print(f"Withdrawal successful. Your new balance is {account['balance']}.")
        else:
            print("There are insufficient funds in the account. Please try a lower amount.")
    else:
        print("Invalid account number. Please try again.")

def check_balance():
    account_number = int(input("Enter your account number: "))
    account = find_account(account_number)
    
    if account:
        print(f"Your current balance is {account['balance']}.")
    else:
        print("Invalid account number. Please try again.")

def show_transaction_history():
    account_number = int(input("Enter your account number: "))
    account = find_account(account_number)

    if account:
        if account["history"]:
            print("Transaction History:")
            for idx, transaction in enumerate(account["history"], start=1):
                print(f"{idx}. {transaction}")
        else:
            print("No transaction history available.")
    else:
        print("Invalid account number. Please try again.")

def find_account(account_number):
    for account in accounts:
        if account["account_number"] == account_number:
            return account
    return None

def exit_program():
    print("Thank you for using the banking system. Goodbye!")
    exit()

commands = {
    'create': create_new_acc,
    'c': create_new_acc,
    'deposit': deposit,
    'd': deposit,
    'withdraw': withdraw_funds,
    'w': withdraw_funds,
    'balance': check_balance,
    'b': check_balance,
    'history': show_transaction_history,
    'h': show_transaction_history,
    'exit': exit_program,
    'e': exit_program
}

def main():
    while True:
        print("\nWelcome to the Banking System Menu:")
        print("1. Create a new account (Type 'create' or 'c')")
        print("2. Deposit funds (Type 'deposit' or 'd')")
        print("3. Withdraw funds (Type 'withdraw' or 'w')")
        print("4. Check balance (Type 'balance' or 'b')")
        print("5. Transaction History (Type 'history' or 'h')")
        print("6. Exit (Type 'exit' or 'e')")

        choice = input("Enter your choice: ").lower()

        if choice in commands:
            commands[choice]()
        else:
            print("Invalid choice. Please enter a valid command.")

if __name__ == "__main__":
    main()
