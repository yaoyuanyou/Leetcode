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
