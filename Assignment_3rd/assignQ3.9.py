# Q 3.9 - Write a Python program for building restaurant menu using class in Python.

class MenuItem:
    """
    Represents a menu item with a name, price, and description.
    """
    def __init__(self, name, price, description):
        """
        Initializes a menu item with a name, price, and description.

        Args:
            name (str): The name of the menu item.
            price (float): The price of the menu item.
            description (str): The description of the menu item.
        """
        self.name = name
        self.price = price
        self.description = description

    def display(self):
        # Displays the menu item.
        print(f"{self.name}: \u20B9{self.price:.2f}")
        print(f"  {self.description}")

class RestaurantMenu:
    # Represents a restaurant menu with a list of menu items.
    def __init__(self):
        # Initializes an empty restaurant menu.
        self.menu_items = []

    def add_item(self, item):
        """
        Adds a menu item to the menu.

        Args:
            item (MenuItem): The menu item to add.
        """
        self.menu_items.append(item)

    def display_menu(self):
        # Displays the restaurant menu.
        print("\nRestaurant Menu:")
        for i, item in enumerate(self.menu_items, start=1):
            print(f"\n{i}.")
            item.display()


def main():
    menu = RestaurantMenu()

    while True:
        print("\nRestaurant Menu Builder")
        print("1. Add menu item")
        print("2. Display menu")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            name = input("Enter menu item name: ")
            price = float(input("Enter menu item price: "))
            description = input("Enter menu item description: ")

            item = MenuItem(name, price, description)
            menu.add_item(item)

        elif choice == "2":
            menu.display_menu()

        elif choice == "3":
            break

        else:
            print("\nInvalid choice")


if __name__ == "__main__":
    main()