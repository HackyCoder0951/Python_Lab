# Q 2.3 - WPA to perform the following operations in tuples :
    # 1 - Find the repeated items in the tuple.
    # 2 - Check if a given element exists in the tuple.
    # 3 - Remove a given element from the tuple.
    # 4 - Convert the tuple to a dictionary.

# Define a sample tuple
sample_tuple = (1, 2, 3, 2, 4, 5, 3, 6, 1, 7)

# Find repeated items
def find_repeated_items(tpl):
    repeated = [item for item in set(tpl) if tpl.count(item) > 1]
    return repeated

# Check whether an element exists in the tuple
def element_exists(tpl, element):
    return element in tpl

# Remove an item from the tuple
def remove_item(tpl, item):
    if item in tpl:
        lst = list(tpl)  # Convert tuple to a list (tuples are immutable)
        lst.remove(item)
        return tuple(lst)  # Convert back to a tuple
    else:
        return tpl  # Return the original tuple if item not found

# Convert a tuple to a dictionary
def tuple_to_dict(tpl):
    if len(tpl) % 2 != 0:
        raise ValueError("Tuple length must be even to convert to a dictionary.")
    return dict(zip(tpl[::2], tpl[1::2]))

# Perform operations
print("Original tuple:", sample_tuple)

# Find repeated items
repeated_items = find_repeated_items(sample_tuple)
print("Repeated items:", repeated_items)

# Check if an element exists
element = 3
exists = element_exists(sample_tuple, element)
print(f"Element {element} exists in tuple:", exists)

# Remove an item from the tuple
item_to_remove = 2
updated_tuple = remove_item(sample_tuple, item_to_remove)
print("Tuple after removing item:", updated_tuple)

# Convert tuple to dictionary
convert_tuple = (1, 'one', 2, 'two', 3, 'three')
converted_dict = tuple_to_dict(convert_tuple)
print("Converted dictionary:", converted_dict)
