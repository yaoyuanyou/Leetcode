#Initial
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        res = 0
        length = len(nums)
        
        for i in range(length):
            j = i + 1
            while j < length:
                if nums[i] == nums[j]:
                    res += 1
                j += 1
        return res
#Combination
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
      res = 0
      hash_map = {}
      
      for i in nums:
        hash_map[i] = hash_map.get(i, 0) + 1
        if hash_map[i] > 1:
          res += hash_map[i] - 1
          
      return res
print(Solution().numIdenticalPairs([1,2,3]))
