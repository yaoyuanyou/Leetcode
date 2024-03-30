# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res_s, res_t = [], []
        for char in s:
            if char != "#":
                res_s.append(char)
            elif res_s:
                res_s.pop()

        for char in t:
            if char != "#":
                res_t.append(char)
            elif res_t:
                res_t.pop()

        return res_s == res_t
