#Time Complexity O(n^2)
#Space Comlexity O(n)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(len(res))
            elif s[i] == ')':
                length = len(res) - stack.pop()
                print(length,res)
                if length > 0:
                    res[-length:] = res[:-length - 1:-1]
            
            else:
                res.append(s[i])
            
        return ''.join(res)
