# Q.7 Python Script to draw the following patterns
#      *           *                *
#     * *          **              **
#    * * *         ***            ***
#   * * * *        ****          ****
#  * * * * *       *****        *****

from recursiveFuncModule import  draw_patterns
print("\nRight-aligned Triangle Pyramid Pattern 1")
rows = int(input("\nEnter the rows you want print : "))
for i in range(1, rows + 1):
    print("* " * i)
print("\nCentered Triangle Pyramid Pattern 2\n")
for i in range(1, rows + 1):
    #Print Spaces to align the start to the right
    print(" " * (rows - i),end=" ")
    print("* " * i)
print("\nLeft-aligned Triangle Pyramid Pattern 3\n")
for i in range(1, rows + 1):
    print("  " * (rows - i),end="")
    print("* " * i)
print("\nDrawing  Patterns function:")
draw_patterns(rows)