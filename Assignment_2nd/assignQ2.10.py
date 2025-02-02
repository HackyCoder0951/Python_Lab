# Q 2.10 - WAP of menu driven of perform matrix addition, substraction and multiplication.

# Function for matrix addition
def matrix_addition(matrix1, matrix2):
    rows, cols = len(matrix1), len(matrix1[0])
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result

# Function for matrix subtraction
def matrix_subtraction(matrix1, matrix2):
    rows, cols = len(matrix1), len(matrix1[0])
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result

# Function for matrix multiplication
def matrix_multiplication(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Matrix multiplication is not possible for the given dimensions.")

    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    return result

# Menu-driven program
def matrix_operations_menu():
    print("Matrix Operations Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    choice = int(input("Enter your choice: "))

    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    print("Enter elements of Matrix 1:")
    matrix1 = [[int(input(f"Enter element ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)]

    print("Enter elements of Matrix 2:")
    matrix2 = [[int(input(f"Enter element ({i+1},{j+1}): ")) for j in range(cols)] for i in range(rows)]

    if choice == 1:
        result = matrix_addition(matrix1, matrix2)
        print("Result of Addition:")
    elif choice == 2:
        result = matrix_subtraction(matrix1, matrix2)
        print("Result of Subtraction:")
    elif choice == 3:
        result = matrix_multiplication(matrix1, matrix2)
        print("Result of Multiplication:")
    else:
        print("Invalid choice.")
        return

    for row in result:
        print(row)
        
if __name__ == "__main__":
     matrix_operations_menu()