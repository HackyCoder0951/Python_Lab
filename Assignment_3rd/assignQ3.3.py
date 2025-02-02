# Q.3 A binary file “book.dat” has structure [BookNo, Book_Name, Author, Price]
    # Write a user define function Create_File( ) to input data for a record and add to book.dat
    # Write a function Count_Rec(Author) in python which accepts the Author name as parameter and count and 
    # return number of books by the given author that are stored in binary file book.dat.

import pickle

def createFile():
    file = open("book.dat","ab")
    BookNo = int(input("\nEnter book number: "))
    Book_Name = input("Enter book Name: ")
    Author =input("Enter author: ").capitalize()
    Price = int(input("Enter price: "))
    record = [BookNo, Book_Name, Author, Price]
    pickle.dump(record, file)
    print("\nRecord added successfully.")
    file.close()


def countRec(Author):
    file = open("book.dat","rb")
    count = 0
    try:
        while True:
            record = pickle.load(file)
            if record[2]==Author:
                count+=1    
    except EOFError:
        pass
    file.close()
    return count


def testProgram():
    while True:
        print("\nPress 1 for adding a new book(record).\nPress 2 for counting the books of a Author.\nPress 3 to exit.")
        try:
            choice = int(input("\nEnter your choice : "))
        except:
            print("\nWARNING :- Please enter a valid numeric value. Thank you.")
        else:
            if choice == 1:
                createFile()
            elif choice == 2:
                Author = input("\nEnter Author name to search : ").capitalize()
                n = countRec(Author)
                print(f"\n{n} books of Author:{Author} are present in the records.")
            elif choice == 3:
                print("\nTHANKS FOR USING THIS PROGRAM.PLEASE COME BACK LATER.\n")
                break
            else:
                print("\nInvalid input : Please enter a valid choice.")


if __name__ == "__main__":
    testProgram() 