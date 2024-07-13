# Cho hai chuỗi s và t, trả về true nếu s là một dãy con của t, ngược lại trả về false.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)