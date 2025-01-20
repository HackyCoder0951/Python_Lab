# Function to implement linear search
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

if __name__ == "__main__":
    arr = [34, 7, 23, 32, 5, 62]
    print("Original array:", arr)
    print("Linear Search (find 23):", linear_search(arr, 23))