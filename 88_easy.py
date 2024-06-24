#O(mlog_2{m})
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n == 0:
            return []

        nums1[m:] = nums2
        nums1.sort()
      
#O(n + m)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
        elif n > 0:
           i, j = m - 1, n - 1
           ind = m + n - 1 

           while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[ind] = nums1[i]
                i -= 1
            else:
                nums1[ind] = nums2[j]
                j -= 1
            ind -= 1
