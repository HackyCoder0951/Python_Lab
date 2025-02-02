# Q 2.4 - WAP to implement binary search.

# Function to implement binary search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    arr = [34, 7, 23, 32, 5, 62]
    print("Original array:", arr)
    print("Binary Search (find 23):", binary_search(sorted(arr), 23))