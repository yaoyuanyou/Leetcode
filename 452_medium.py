#Initial 5%
class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        traverse = set()
        length = len(nums)
        for i in range(length):
            if i in traverse:
                continue
            traverse.add(i)
            j = i
            local = set()

            while True:
                local.add(j)
                #print(j)
                j = (j + nums[j]) % length
                #print(j)
                if (j == i and len(local) == 1) or (nums[i] < 0 and nums[j] > 0) or (nums[i] > 0 and nums[j] < 0):
                    break

                if j in local:
                    if j == i:
                        return True
                    else:
                        i = j
                        local = set()
        
        return False


#Optimization
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n, visited = len(nums), set()
        for i in range(n):
            if i not in visited:
                local_s = set()
                while True:
                    if i in local_s: 
                        return True
                    if i in visited: 
                        break          
                    visited.add(i)
                    local_s.add(i)
                    prev = i
                    i = (i + nums[i]) % n
                    if prev == i or nums[i]*nums[prev]<0: 
                        break
        return False

#Optimization Space Complexity O(1)
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        def next_index(idx, lst = nums):
            return (idx + lst[idx]) % n

        for i in range(n):
            if isinstance(nums[i], int):
                index = i
                if nums[i] > 0:
                    while True:
                        nxt_idx = next_index(index)
        
                        if nums[nxt_idx] == str(i):
                            return True
                        elif isinstance(nums[nxt_idx], str):
                            nums[index] = str(i)
                            break
                        else:
                            if nums[nxt_idx] < 0 or nxt_idx == index:
                                nums[index] = str(i)
                                break   

                            nums[index] = str(i)
                            index = nxt_idx



                else:
                    while True:
                        nxt_idx = next_index(index)
                        
                        if nums[nxt_idx] == str(i):
                            return True
                        elif isinstance(nums[nxt_idx], str):
                            nums[nxt_idx] = str(i)
                            break
                        else:
                            if nums[nxt_idx] > 0 or nxt_idx == index:
                                nums[index] = str(i)
                                break   

                            nums[index] = str(i)
                            index = nxt_idx
                        
                        

        return False
                            
