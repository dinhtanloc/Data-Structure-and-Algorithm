from collections import defaultdict
def longestCommonPrefix(strs):
        ans=""
        v=sorted(strs)
        first=v[0]
        last=v[-1]
        print(first)
        print(last)
        print(min(len(first)))
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 

strs=["dog","racecar","car"]

print(longestCommonPrefix(strs))
        