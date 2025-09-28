from operation import deposit, withdraw, check_balance
from utils import get_amount, get_pin

def main():
    print("=== Simple ATM Simulator ===")
    balance = 0
    pin_code = "1234"

    # Ask for PIN
    entered_pin = get_pin("Enter PIN: ")
    if entered_pin != pin_code:
        print(" Wrong PIN! Access denied.")
        return

    print("✅ PIN accepted!")

    while True:
        print("\nOptions: 1.Deposit | 2.Withdraw | 3.Check Balance | 4.Quit")
        choice = input("Choose an option: ").strip()

        if choice == "4":
            print("Thank you for using the ATM!")
            break

        if choice == "1":
            amt = get_amount("Enter deposit amount: ")
            balance = deposit(balance, amt)
        elif choice == "2":
            amt = get_amount("Enter withdraw amount: ")
            balance = withdraw(balance, amt)
        elif choice == "3":
            check_balance(balance)
        else:
            print(" Invalid option, try again.")

if __name__ == "__main__":
    main()
