# // first approach
# function fn(arr, k):
#     curr = some data type to track the window

#     // build the first window
#     for i in [0, k - 1]:
#         Do something with curr or other variables to build first window

#     ans = answer variable, might be equal to curr here depending on the problem
#     for i in [k, arr.length - 1]:
#         Add arr[i] to window
#         Remove arr[i - k] from window
#         Update ans

#     return ans

#  second approach
# function fn(arr, k):
#     curr = some data type to track the window
#     ans = answer variable
#     for i in range(len(arr)):
#         if i >= k:
#             Update ans
#             Remove arr[i - k] from window
#         Add arr[i] to window

#     Update ans    
#     return ans // Alternatively, you could do something like return max(ans, curr) if the problem is asking for a maximum value and curr is tracking that.

def find_best_subarray(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]
    
    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    
    return ans