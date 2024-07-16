def counting_sort(arr):
    # Tìm giá trị lớn nhất trong mảng để xác định phạm vi của mảng đếm
    max_val = max(arr)
    
    # Khởi tạo mảng đếm
    count = [0] * (max_val + 1)
    
    # Đếm số lần xuất hiện của mỗi phần tử trong mảng gốc
    for num in arr:
        count[num] += 1
    
    # Sử dụng mảng đếm để sắp xếp mảng
    sorted_index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[sorted_index] = i
            sorted_index += 1
            count[i] -= 1

# Ví dụ sử dụng thuật toán counting sort
arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print("Danh sách đã sắp xếp:", arr)
