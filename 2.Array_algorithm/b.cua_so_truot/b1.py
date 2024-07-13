# ### Bài 1
# Cho một mảng số nguyên dương nums và một số nguyên k.

# Tìm độ dài của mảng con dài nhất có tổng nhỏ hơn hoặc bằng k.
def find_length(nums, k):
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans