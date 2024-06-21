class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set = set(nums)
        num_max = -1
        for x in nums:
            if x > num_max and -x in num_set:
                num_max = x
        return num_max
