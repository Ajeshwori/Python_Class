from calculator.operation import add, subtract, multiply, divide
from calculator.utils import get_number

def main():
    print("=== Simple Calculator ===")
    while True:
        print("\nOptions : +, -, *, /, q (quit)")
        choice = input("Choose an operation: ").strip()

        if choice == "q":
            print("Exiting ... Goodbye") 
            break

        if choice not in ['+', '-', '*', '/']:
            print("Invalid option")
            continue
        
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == "+":
            print("Result: ", add(num1, num2))
        elif choice == "-":
            print("Result: ", subtract(num1, num2))
        elif choice == "*":
            print("Result: ", multiply(num1, num2))
        elif choice == "/":
            print("Result: ", divide(num1, num2)) 

if __name__ == "__main__":
    main()

