class Calculator:
    def __init__(self):
        self.result = 0.0

    def add(self, x, y):
        self.result = x + y

    def subtract(self, x, y):
        self.result = x - y

    def multiply(self, x, y):
        self.result = x * y

    def divide(self, x, y):
        if y == 0:
            self.result = "Division by zero is not allowed."
        else:
            self.result = x / y

    def display_result(self):
        print("Result:", self.result)

def get_user_input():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

def get_operation_choice():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    return input("Enter choice (1/2/3/4): ")

def main():
    calculator = Calculator()

    while True:
        num1, num2 = get_user_input()
        choice = get_operation_choice()

        if choice == '1':
            calculator.add(num1, num2)
        elif choice == '2':
            calculator.subtract(num1, num2)
        elif choice == '3':
            calculator.multiply(num1, num2)
        elif choice == '4':
            calculator.divide(num1, num2)
        else:
            print("Invalid choice. Please select a valid operation (1/2/3/4).")
            continue

        calculator.display_result()

        restart = input("Do you want to perform another calculation? (yes/no): ")
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
