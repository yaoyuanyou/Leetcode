#Initial
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k != 0 and len(nums) > 1:
            k = min(k, len(nums) - 1)
            hashmap = {}

            for ind, num in enumerate(nums[0: k + 1]):
                if num not in hashmap:
                    hashmap[num] = ind
                else:
                    return True
            
            i = 1

            while i + k < len(nums):
                if hashmap.get(nums[i + k], 0) >= i:
                    return True
                hashmap[nums[i + k]] = i + k
                i += 1
        return False

#Clean and concise
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if i - hashmap.get(nums[i], - k - 1) <= k:
                return True
            hashmap[nums[i]] = i

        return False
