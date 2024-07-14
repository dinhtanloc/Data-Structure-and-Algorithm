def strStr(haystack, needle):
    if not needle:
        return -1  # Nếu needle là chuỗi rỗng, trả về 0 theo quy ước

    n, m = len(haystack), len(needle)

    if m > n:
        return -1  # Nếu needle dài hơn haystack, không thể có needle trong haystack

    # Duyệt qua các chỉ số trong haystack nơi needle có thể bắt đầu
    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i

    return -1
    


        
haystack ='hello'
needle ='ll'
print(strStr(haystack,needle))