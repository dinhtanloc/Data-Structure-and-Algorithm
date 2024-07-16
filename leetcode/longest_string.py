def lengthOfLongeststring(s):
    if not s:
        return 0
    
    ans = 0
    ans_list = []
    
    for char in s:
        if char in ans_list:
            index = ans_list.index(char)
            ans_list = ans_list[index + 1:]
        ans_list.append(char)
        ans = max(ans, len(ans_list))
    
    return ans
        
s="pwwkew"
print(lengthOfLongeststring(s))