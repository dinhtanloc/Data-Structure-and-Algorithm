def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Khởi tạo khoảng cách ban đầu

    # Giảm dần khoảng cách đến 1
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Sắp xếp các phần tử cách nhau bởi khoảng cách gap
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Giảm khoảng cách
    return arr

# Ví dụ sử dụng thuật toán shell sort
arr = [12, 34, 54, 2, 3]
sorted_arr = shell_sort(arr)
print("Danh sách đã sắp xếp:", sorted_arr)
