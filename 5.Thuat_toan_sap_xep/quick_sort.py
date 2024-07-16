def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Ví dụ sử dụng thuật toán quick sort
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quick_sort(arr)
print("Danh sách đã sắp xếp:", sorted_arr)
