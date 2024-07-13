# ### Bài 2
# Cho một chuỗi nhị phân s. Chỉ có duy nhất một lần chuyển 0 thành 1. Sau khi thực hiện việc chuyển, độ dài của chuỗi con dài nhất chỉ chứa 1 là bao nhiêu?
def find_length(s):
    left = curr = ans = 0 
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans