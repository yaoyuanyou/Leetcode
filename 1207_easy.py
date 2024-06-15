class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if len(arr) == 1:
            return True
        
        index = 0
        occur = set()
        sorted_list = sorted(arr)
        prev = sorted_list[0]

        for i in range(1, len(arr)):

            if sorted_list[i] > prev:
                if i - index in occur:
                    return False
                else:
                    occur.add(i - index)
                    index = i
                    prev = sorted_list[i]
        
        if sorted_list[-1] == prev and len(arr) - index in occur:
            return False

        return True
