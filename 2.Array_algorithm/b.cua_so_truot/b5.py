def twoSum(nums, target):
    left=cur=0
    l=0
    r=len(nums)-1
    while l<r:
        if (nums[l]+nums[r])==target:
            return [l,r]
        l+=1
        r-=1 
    for right in range(len(nums)):
        cur+=nums[right]
        while cur !=target and left < right:
            cur-=nums[left]
            left+=1
            if cur==target:
                break
        if cur==target:
            return [left,right]
    return

nums=[3,2,3]
target=6
print(twoSum(nums=nums,target=target))