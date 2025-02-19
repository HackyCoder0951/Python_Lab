# Q 3.5 - Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.

class Bank:
    """
    Represents a bank.
    """
    def __init__(self):
        """
        Initializes a bank with an empty dictionary of customers.
        """
        self.customers = {}

    def add_customer(self, customer_id, name, city, balance):
        """
        Adds a new customer to the bank.

        Args:
            customer_id (str): The ID of the customer.
            name (str): The name of the customer.
            city (str): The city of the customer.
            balance (float): The initial balance of the customer's account.
        """
        self.customers[customer_id] = {"name": name, "city":city, "balance": balance}

    def remove_customer(self, customer_id):
        """
        Removes a customer from the bank.

        Args:
            customer_id (str): The ID of the customer to remove.
        """
        if customer_id in self.customers:
            del self.customers[customer_id]
        else:
            print("Customer not found.")

    def deposit(self, customer_id, amount):
        """
        Deposits money into a customer's account.

        Args:
            customer_id (str): The ID of the customer.
            amount (float): The amount to deposit.
        """
        if customer_id in self.customers:
            self.customers[customer_id]["balance"] += amount
        else:
            print("Customer not found.")

    def withdraw(self, customer_id, amount):
        """
        Withdraws money from a customer's account.

        Args:
            customer_id (str): The ID of the customer.
            amount (float): The amount to withdraw.
        """
        if customer_id in self.customers:
            if self.customers[customer_id]["balance"] >= amount:
                self.customers[customer_id]["balance"] -= amount
            else:
                print("Insufficient balance.")
        else:
            print("Customer not found.")

    def check_balance(self, customer_id):
        """
        Checks the balance of a customer's account.

        Args:
            customer_id (str): The ID of the customer.
        """
        if customer_id in self.customers:
            print(f"Balance: {self.customers[customer_id]['balance']}")
        else:
            print("Customer not found.")

    def display_customers(self):
        """
        Displays all customers in the bank.
        """
        if not self.customers:
            print("No customers found.")
        else:
            for customer_id, customer in self.customers.items():
                print(f"Customer ID: {customer_id}")
                print(f"Name: {customer['name']}")
                print(f"City: {customer['city']}")
                print(f"Balance: {customer['balance']}")
                print()


def main():
    bank = Bank()

    while True:
        print("\nBank Management System")
        print("1. Add customer")
        print("2. Remove customer")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check balance")
        print("6. Display customers")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == "1":
            customer_id = input("\nEnter customer ID: ")
            name = input("Enter customer name: ")
            city = input("Enter customer city: ")
            balance = float(input("Enter initial balance: "))
            bank.add_customer(customer_id, name, city, balance)

        elif choice == "2":
            customer_id = input("\nEnter customer ID to remove: ")
            bank.remove_customer(customer_id)

        elif choice == "3":
            customer_id = input("\nEnter customer ID: ")
            # features : - print current balance here
            amount = float(input("Enter amount to deposit: "))
            # update : - print confirmations message here
            bank.deposit(customer_id, amount)

        elif choice == "4":
            customer_id = input("\nEnter customer ID: ")
            # features : - print current balance here
            amount = float(input("Enter amount to withdraw: "))
            # update : - print confirmations message here
            bank.withdraw(customer_id, amount)

        elif choice == "5":
            customer_id = input("\nEnter customer ID: ")
            bank.check_balance(customer_id)

        elif choice == "6":
            print("\nCustomers:")   
            bank.display_customers()

        elif choice == "7":
            break

        else:
            print("\nInvalid choice")


if __name__ == "__main__":
    main()