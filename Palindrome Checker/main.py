from operation import is_palindrome
from utils import get_input

def main():
    print("=== Palindrome Checker ===")

    while True:
        text = get_input("\nEnter a word/number (or 'q' to quit): ")

        if text.lower() == "q":
            print(" Exiting... Goodbye!")
            break

        if is_palindrome(text):
            print(f" '{text}' is a palindrome!")
        else:
            print(f"'{text}' is not a palindrome.")

if __name__ == "__main__":
    main()
