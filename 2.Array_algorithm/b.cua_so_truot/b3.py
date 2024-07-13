# ### Bài 3 Số lượng mảng con
# Cho một mảng số nguyên dương nums và một số nguyên k.

# Hãy trả về số lượng mảng con chứa các phần tử được xếp đúng theo thứ tự của mảng gốc, trong đó tích của tất cả các phần tử trong mảng con nhỏ hơn k.
class Solution:
    nums = [10, 5, 2, 6] 
    k = 100
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1

        return ans