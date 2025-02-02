# Q 3.6 - Write a Python program to define a class that can add and subtract two numbers.

class Calculator:
    """
    Represents a calculator that can add and subtract two numbers.
    """
    def __init__(self):
        """
        Initializes a calculator.
        """
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num2 == 0:
            print("\nError: Division by zero is not allowed.")
            return
        return num1 / num2
    
    def modulus(self, num1, num2):
        if num2 == 0:
            print("\nError: Division by zero is not allowed.")
            return
        return num1 % num2
    
    def power(self, num1, num2):
        return num1 ** num2


def main():
    calculator = Calculator()

    while True:
        print("\nCalculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("\n Enter your choice : ")

        if choice == "1":
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"\nResult: {calculator.add(num1, num2)}")

        elif choice == "2":
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"\nResult: {calculator.subtract(num1, num2)}")

        elif choice == "3":
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"\nResult: {calculator.multiply(num1, num2)}")

        elif choice == "4":
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"\nResult: {calculator.divide(num1, num2)}")
        
        elif choice == "5":
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"\nResult: {calculator.modulus(num1, num2)}")

        elif choice == "6":
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
            print(f"\nResult: {calculator.power(num1, num2)}")

        elif choice == "7":
            break

        else:
            print("\nInvalid choice")


if __name__ == "__main__":
    main()