#Initial
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def palindrome(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i, j = 0 , len(s) - 1
        ind = False

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif ind:
                return False
            else:
                ind = True
                if s[i + 1] == s[j] and s[i] == s[j - 1]:
                    return palindrome(s[i + 1: j + 1]) or palindrome(s[i: j])
                elif s[i + 1] == s[j]:
                    i += 2
                    j -= 1
                elif s[i] == s[j - 1]:
                    i += 1
                    j -= 2
                else:
                    return False

        return True

#Faster
class Solution:
    def validPalindrome(self, s: str) -> bool:

        i, j = 0 , len(s) - 1
        ind = False

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if s[i + 1] == s[j] or s[i] == s[j - 1]:
                    return s[i + 1: j + 1] == s[i + 1: j + 1][::-1] or s[i: j] == s[i: j][::-1]
                return False
        return True

        
