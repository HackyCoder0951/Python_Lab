# Q 3.8 - Create a Time class and initialize it with hours and minutes.
    # Make a method add_Time which should take two time object and add them. 
        # E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
    # Make a method display_Time which should print the time.
    # Make a method Display_Minute which should display the total minutes in the Time.
        # E.g.- (1 hr 2 min) should display 62 minute.

class Time:
    """
    Represents a time with hours and minutes.
    """
    def __init__(self, hours, minutes):
        """
        Initializes a time with hours and minutes.

        Args:
            hours (int): The hours of the time.
            minutes (int): The minutes of the time.
        """
        self.hours = hours
        self.minutes = minutes

    def add_time(self, other_time):
        """
        Adds two times.

        Args:
            other_time (Time): The time to add.

        Returns:
            Time: The sum of the two times.
        """
        total_minutes = self.to_minutes() + other_time.to_minutes()
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return Time(hours, minutes)

    def display_time(self):
        """
        Displays the time.
        """
        print(f"{self.hours} hours and {self.minutes} minutes")

    def display_minutes(self):
        """
        Displays the total minutes in the time.
        """
        print(f"{self.to_minutes()} minutes")

    def to_minutes(self):
        """
        Converts the time to total minutes.

        Returns:
            int: The total minutes in the time.
        """
        return self.hours * 60 + self.minutes


def main():
    while True:
        print("\nTime Calculator")
        print("1. Add time")
        print("2. Display time")
        print("3. Display minutes")
        print("4. Exit")

        choice = input("\nEnter your choice (1/2/3/4): ")

        if choice == "1":
            hours1 = int(input("Enter hours for time 1: "))
            minutes1 = int(input("Enter minutes for time 1: "))
            hours2 = int(input("Enter hours for time 2: "))
            minutes2 = int(input("Enter minutes for time 2: "))

            time1 = Time(hours1, minutes1)
            time2 = Time(hours2, minutes2)

            print("\nTime 1:")
            time1.display_time()
            print("\nTime 2:")
            time2.display_time()

            time3 = time1.add_time(time2)
            print("\nTotal Time ( T1 + T2 ):")
            time3.display_time()

        elif choice == "2":
            hours = int(input("Enter hours: "))
            minutes = int(input("Enter minutes: "))

            time = Time(hours, minutes)
            print("\nEntered Time:")
            time.display_time()

        elif choice == "3":
            hours = int(input("Enter hours: "))
            minutes = int(input("Enter minutes: "))

            time = Time(hours, minutes)
            print("\nTotal Minutes:")
            time.display_minutes()

        elif choice == "4":
            break

        else:
            print("\nInvalid choice")


if __name__ == "__main__":
    main()