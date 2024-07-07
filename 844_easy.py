# https://leetcode.com/problems/backspace-string-compare/
#Stack
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

#Two Pointers
#Time Complexity O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        n, m = len(s) - 1, len(t) - 1

        while n >= 0 or m >= 0:

            skip = 0
            while n >= 0:
                if s[n] != "#":
                    if skip > 0:
                        skip -= 1
                    else:
                        break
                else:
                    skip += 1
                
                n -= 1
            
            skip = 0
            while m >= 0:
                if t[m] != "#":
                    if skip > 0:
                        skip -= 1
                    else:
                        break
                else:
                    skip += 1
                
                m -= 1

            if n < 0 and m < 0:
                return True
            elif n < 0 or m < 0:
                return False
            else:
                print(s[n], t[m], n, m)
                if s[n] != t[m]:
                    return False
            n -= 1
            m -= 1
        
        return True
