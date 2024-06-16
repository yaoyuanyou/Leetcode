#Initial
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 0
        
        i, index = 1, 0
        count = []

        while i < len(s):
            if s[i] != s[i - 1]:
                count.append(i - index)
                index = i
            i += 1
        count.append(len(s) - index)

        res = 0
        for i in range(1, len(count)):
            res += min(count[i], count[i - 1])

        return res

#Faster
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) < 2:
            return 0

        count = 1 
        ans = 0
        prev = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                prev = count
                count = 1

            if prev >= count:
                ans += 1
        
        return ans
