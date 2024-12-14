# Q.8 max or min from the list ?

from recursiveFuncModule import find_max_min,find_max_recursive,find_min_recursive

n=int(input("Enter the total number of element in the list : "))
if(n<=0):
    print("The list is empty, Please enter a valid number greater than 0")
else:
    num_list=[]
    for i in range(n):
        value=int(input(f"Enter {i+1} element : "))
        num_list.append(value)

    maximum = num_list[0]
    minimum = num_list[0]
    for i in range(n):
        if(maximum<num_list[i]):
            maximum=num_list[i]
        if(minimum>num_list[i]):
            minimum=num_list[i]
    
    print("List of elements :",num_list,"\n")
    
    print("Maximum value from the list :",maximum,"")
    print("Minimum value from the list :",minimum,"\n")
    
    print("Minimum & Maximum value from the list using function:",find_max_min(num_list),"\n")
    print("Maximum value from the list using function :",find_max_recursive(num_list),"\n")
    print("Minimum value from the list using function :",find_min_recursive(num_list),"\n")