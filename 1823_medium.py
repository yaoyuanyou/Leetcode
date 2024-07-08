#Time Complexity O(n^2)
#Space Complexity O(n)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        lst = [i for i in range(1, n + 1)]
        index, i = 0, 1
        
        while i <= n - 1:
            idx = k
            
            while idx > 0:
                if lst[index] != 0:
                    idx -= 1

                index += 1

                if index == n:
                    index = 0
            
            lst[index - 1] = 0
            i += 1
        
        return sum(lst)

#Recursion Time Complexity O(n)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def recursion(n, k):
            if n == 1:
                return 0
            return (recursion(n - 1, k) + k) % n

        return recursion(n, k) + 1

#Space Complexity O(1)
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0
        for i in range(2, n + 1):
            res = (res + k) % i
        return res + 1
