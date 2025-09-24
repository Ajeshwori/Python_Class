def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))   
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")


