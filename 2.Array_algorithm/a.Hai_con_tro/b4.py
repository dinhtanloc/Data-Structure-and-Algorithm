# Gộp hai mảng đã sắp xếp thành một mảng mới có thứ tự
# Cho hai mảng số nguyên đã sắp xếp.

# Trộn hai mảng và trả về mảng mới cũng được sắp xếp.

def combine(arr1, arr2):
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    
    return ans