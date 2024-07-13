# Kiểm tra chuỗi palindrome
# Viết hàm trả về true nếu chuỗi là palindrome, nếu không trả về false.
def check_if_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

check_if_palindrome('TekkeT')