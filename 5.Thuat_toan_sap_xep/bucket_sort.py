def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Bước 1: Tạo các bucket (giỏ)
    bucket_count = len(arr)
    max_val = max(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Bước 2: Phân phối các phần tử vào các bucket
    for num in arr:
        index = int(num * bucket_count / (max_val + 1))
        buckets[index].append(num)

    # Bước 3: Sắp xếp các phần tử trong mỗi bucket
    for bucket in buckets:
        bucket.sort()

    # Bước 4: Nối các bucket đã sắp xếp lại với nhau
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Ví dụ sử dụng thuật toán bucket sort
arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_arr = bucket_sort(arr)
print("Danh sách đã sắp xếp:", sorted_arr)
