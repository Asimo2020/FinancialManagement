transactions = []
def add_transaction():
    title = input("Enter transaction title: ")
    amount = float(input("Enter transaction amount: "))
    transactions.append((title, amount))
    print("Transaction added successfully!\n")
def show_transactions():
    if not transactions:
        print("No transactions to show.\n")
    else:
        for idx, (title, amount) in enumerate(transactions, start=1):
            print(f"{idx}. {title}: {amount}")
        print()
def calculate_balance():
    balance = sum([amount for _, amount in transactions])
    return balance
# Main program loop
while True:
    print("1. Add a transaction")
    print("2. Show all transactions")
    print("3. Calculate current balance")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_transaction()
    elif choice == '2':
        show_transactions()
    elif choice == '3':
        balance = calculate_balance()
        print(f"Current balance: {balance}\n")
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")