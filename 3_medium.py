#Initial
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        
        hashmap = {}
        left_ind = 0
        res = 1
        for i in range(len(s)):
            if s[i] not in hashmap and i < len(s) - 1:
                hashmap[s[i]] = i
            elif s[i] not in hashmap and i == len(s) - 1:
                res = max(res, i + 1 - left_ind)
            elif hashmap[s[i]] < left_ind and i < len(s) - 1:
                hashmap[s[i]] = i
            elif hashmap[s[i]] < left_ind and i == len(s) - 1:
                res = max(res, i + 1 - left_ind)
            else:
                res = max(res, i - left_ind)
                left_ind = hashmap[s[i]] + 1
                hashmap[s[i]] = i
        return res

#Faster
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) < 2:
            return 1

        left_index = 0
        res = 0
        hashmap = {}

        for i in range(len(s)):
            if s[i] in hashmap and left_index <= hashmap[s[i]]:
                res = max(res, i - left_index)
                left_index = hashmap[s[i]] + 1
                
            hashmap[s[i]] = i

        res = max(res, len(s) - left_index)
        return res
