# Q 3.4 - Write a Python program to create a class that represents a shape. 
# Include methods to calculate its area and perimeter. 
# Implement subclasses for different shapes like circle, triangle, and square.

import math

class Shape:
    """
    Base class for all shapes.
    """
    def __init__(self):
        pass

    def area(self):
        """
        Calculates the area of the shape.
        """
        pass

    def perimeter(self):
        """
        Calculates the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Represents a circle.
    """
    def __init__(self, radius):
        """
        Initializes a circle with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Triangle(Shape):
    """
    Represents a triangle.
    """
    def __init__(self, side1, side2, side3):
        """
        Initializes a triangle with three sides.

        Args:
            side1 (float): The length of the first side.
            side2 (float): The length of the second side.
            side3 (float): The length of the third side.
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        """
        Calculates the area of the triangle using Heron's formula.

        Returns:
            float: The area of the triangle.
        """
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        """
        Calculates the perimeter of the triangle.

        Returns:
            float: The perimeter of the triangle.
        """
        return self.side1 + self.side2 + self.side3


class Square(Shape):
    """
    Represents a square.
    """
    def __init__(self, side):
        """
        Initializes a square with a given side length.

        Args:
            side (float): The length of the side.
        """
        self.side = side

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.side ** 2

    def perimeter(self):
        """
        Calculates the perimeter of the square.

        Returns:
            float: The perimeter of the square.
        """
        return 4 * self.side


def main():
    while True:
        print("\nShape Calculator")
        print("1. Circle")
        print("2. Triangle")
        print("3. Square")
        print("4. Exit\n")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            radius = float(input("Enter the radius of the circle: "))
            circle = Circle(radius)
            print(f"\nCircle area: {circle.area()}")
            print(f"Circle perimeter: {circle.perimeter()}")
            main()

        elif choice == "2":
            side1 = float(input("\n Enter the length of the first side of the triangle: "))
            side2 = float(input("Enter the length of the second side of the triangle: "))
            side3 = float(input("Enter the length of the third side of the triangle: "))
            triangle = Triangle(side1, side2, side3)
            print(f"\nTriangle area: {triangle.area()}")
            print(f"Triangle perimeter: {triangle.perimeter()}")
            main()

        elif choice == "3":
            side = float(input("\n Enter the length of the side of the square: "))
            square = Square(side)
            print(f"\nSquare area: {square.area()}")
            print(f"Square perimeter: {square.perimeter()}")
            main()

        elif choice == "4":
            print("\nTHANKS FOR USING THIS PROGRAM.PLEASE COME BACK LATER.\n")
            break
        
        else:
            print("Invalid choice")
            main()


if __name__ == "__main__":
    main()