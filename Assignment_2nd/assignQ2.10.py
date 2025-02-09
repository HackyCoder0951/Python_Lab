# Q 2.10 - WAP of menu driven of perform mat addition, substraction and multiplication.

# Function for mat addition
def mat_add(m1, m2):
    ro, co = len(m1), len(m1[0])
    result = [[m1[i][j] + m2[i][j] for j in range(co)] for i in range(ro)]
    return result

# Function for mat subtraction
def mat_sub(m1, m2):
    ro, co = len(m1), len(m1[0])
    result = [[m1[i][j] - m2[i][j] for j in range(co)] for i in range(ro)]
    return result

# Function for mat multiplication
def mat_mul(m1, m2):
    ro1, co1 = len(m1), len(m1[0])
    ro2, co2 = len(m2), len(m2[0])

    if co1 != ro2:
        raise ValueError("mat multiplication is not possible for the given dimensions.")

    result = [[sum(m1[i][k] * m2[k][j] for k in range(co1)) for j in range(co2)] for i in range(ro1)]
    return result

# Menu-driven program
def mat_opr_menu():
    print("Matrix Operations Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    choice = int(input("Enter your choice: "))

    ro = int(input("Enter the number of ro: "))
    co = int(input("Enter the number of columns: "))

    print("Enter elements of mat 1:")
    m1 = [[int(input(f"Enter element ({i+1},{j+1}): ")) 
           for j in range(co)] for i in range(ro)]

    print("Enter elements of mat 2:")
    m2 = [[int(input(f"Enter element ({i+1},{j+1}): ")) 
           for j in range(co)] for i in range(ro)]

    if choice == 1:
        result = mat_add(m1, m2)
        print("Result of Addition:")
    elif choice == 2:
        result = mat_sub(m1, m2)
        print("Result of Subtraction:")
    elif choice == 3:
        result = mat_mul(m1, m2)
        print("Result of Multiplication:")
    else:
        print("Invalid choice.")
        return

    for row in result:
        print(row)
        
if __name__ == "__main__":
     mat_opr_menu()