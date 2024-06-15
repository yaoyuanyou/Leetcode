#Initial
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) < 2:
            return 1
        
        res = 0
        index = 0
        prev = s[0]
        
        for i in range(1, len(s)):
            if s[i] != prev:
                res = max(res ,i - index)
                prev = s[i]
                index = i

        res = max(res, len(s) - index)
        return res

#Simple
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) < 2:
            return 1
        
        res = 1
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
                res = max(res, count)
            else:
                count = 1

        return res
