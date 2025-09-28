def deposit(balance, amount):
    balance += amount
    print(f"Deposited {amount}. New balance: {balance}")
    return balance

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f" Withdrew {amount}. New balance: {balance}")
    return balance

def check_balance(balance):
    print(f" Current balance: {balance}")
