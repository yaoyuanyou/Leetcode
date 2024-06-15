class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashmap = {}
        res = 0
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for key, value in hashmap.items():
            if value < 2:
                res += key
        return res
