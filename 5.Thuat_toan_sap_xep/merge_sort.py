def merge_sort(arr):
    if len(arr) > 1:
        # Chia danh sách thành hai nửa
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Đệ quy gọi merge_sort cho từng nửa
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Gộp hai nửa đã được sắp xếp
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Kiểm tra xem còn phần tử nào chưa được gộp không
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Ví dụ sử dụng thuật toán merge sort
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Danh sách đã sắp xếp:", arr)
