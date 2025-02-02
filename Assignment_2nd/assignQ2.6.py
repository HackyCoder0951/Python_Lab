# Q 2.6 - WAP to program to implement selection sort.

# Function to implement selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    arr = [34, 7, 23, 32, 5, 62]
    print("Original array:", arr)
    print("Selection Sort:", selection_sort(arr.copy()))