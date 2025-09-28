def get_amount(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Amount must be greater than 0!")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_pin(prompt):
    return input(prompt).strip()
