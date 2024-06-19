class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        count = 1
        ind = 1
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == prev:
                count += 1
                if count == 2: 
                    nums[ind] = nums[i]
                    ind += 1
            else:
                prev = nums[i]
                nums[ind] = nums[i]
                count = 1
                ind += 1

        return ind



#pop for index, remove for element
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        
        while i < len(nums) - 2:
            if nums[i] == nums[i + 1] and nums[i] == nums[i + 2]:
                nums.pop(i + 2)
            else:
                i += 1
        return len(nums)    

#clear
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
