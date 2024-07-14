def isPalindrome(x):
    num_list=str(x)
    left=0
    right =len(num_list)-1
    while left<right:
        if num_list[left] != num_list[right]:
            return False
        left+=1
        right-=1
    return True

