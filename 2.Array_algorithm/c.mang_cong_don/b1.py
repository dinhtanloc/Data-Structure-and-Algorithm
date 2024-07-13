# ### Bài 1

# Cho một mảng số nguyên nums, một mảng queries trong đó queries[i] = [x, y] và một số nguyên limit.

# Hãy tạo mảng boolean trả về kết quả của từng truy vấn.

# Một truy vấn là true nếu tổng của mảng con từ x đến y nhỏ hơn limit, ngược lại là false.

def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]## suy luan
        ans.append(curr < limit)

    return ans