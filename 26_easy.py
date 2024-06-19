#Initial
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set(nums)
        sorted_list = sorted(unique)
        length = len(unique)
        for i in range(length):
            nums[i] = sorted_list[i]

        return length

#Slower
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        left = 0
        res = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[left]:
                left += 1
                res += 1
                nums[left] = nums[i]

        return res
