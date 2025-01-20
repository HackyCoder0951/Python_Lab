# Function to implement shell sort
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

if __name__ == "__main__":
    arr = [34, 7, 23, 32, 5, 62]
    print("Original array:", arr)
    print("Shell Sort:", shell_sort(arr.copy()))