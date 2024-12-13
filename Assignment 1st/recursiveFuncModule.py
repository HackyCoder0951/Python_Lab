num_list=[]


def add_numbers(num):
    t_sum = 0
    for i in range(num):
        value = int(input(f"Enter {i+1} element : "))
        num_list.append(value)  # assigning values into num_list[]
        t_sum += value
    return t_sum

def add_numbers_recursive(rec_num, index=0):
    if index >= rec_num:  # Base case: if index is equal to num, return 0
        return 0
    else:
        value = int(input(f"Enter {index + 1} element: "))
        num_list.append(value)  # Assigning values into num_list[]
        return value + add_numbers_recursive(rec_num, index + 1)  # Recursive call

