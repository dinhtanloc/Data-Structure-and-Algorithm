def print_array(arr):
    for elem in arr:
        print(elem, end=" ")
    print()

def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    arr = [6, 1, 5, 8, 4]
    insertion_sort(arr)
    print("Mảng sau khi sắp xếp là:")
    print_array(arr)
