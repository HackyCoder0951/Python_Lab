# Python Script to draw the following patterns
#      *           *                *
#     * *          **              **
#    * * *         ***            ***
#   * * * *        ****          ****
#  * * * * *       *****        *****

print("\nPattern 1")
rows = int(input("\nEnter the rows you want print : "))

for i in range(1, rows + 1):
    #Print Spaces to align the start to the right
    print(" " * (rows - i),end=" ")
    #
    print("* " * i)

print("\nPattern 2\n")
for i in range(1, rows + 1):
    #
    print("* " * i)

print("\nPattern 3\n")
for i in range(1, rows + 1):
    #
    print("  " * (rows - i),end="")

    print("* " * i)
