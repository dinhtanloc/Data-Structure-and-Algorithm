# Cặp số có tổng bằng một số cho trước
# Cho một mảng đã sắp xếp gồm các số nguyên phân biệt và số nguyên target.

# Trả về true nếu tồn tại một cặp số có tổng bằng target, ngược lại trả về false.
def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1
    
    return False

nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13
check_for_target(nums=nums,target=target)
