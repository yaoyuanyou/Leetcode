#O(n) and O(n)
def min_merge_operations(nums):
    l, r = 0, len(nums) - 1
    
    if l == r:
        return 0
    
    res = 0
    
    while l < r:
        if r - l == 1:
            if nums[l] == nums[r]:
                return 0
            else:
                return 1
            
        if nums[l] == nums[r]:
            l += 1
            r -= 1

        elif nums[l] < nums[r]:
            res += 1
            nums[l + 1] = nums[l] + nums[l + 1]
            res += min_merge_operations(nums[l + 1 : r + 1])
            break
        else:
            res += 1
            nums[r - 1] = nums[r] + nums[r - 1]
            res += min_merge_operations(nums[l: r])
            break
        
    return res

#O(n) and O(1)
def min_merge_operations(nums):
    l, r = 0, len(nums) - 1
    l_cnt, r_cnt = nums[l], nums[r]
    
    if l == r:
        return 0
    
    res = 0
    
    while l < r:
        if l_cnt == r_cnt:
            l += 1
            r -= 1
            l_cnt, r_cnt = nums[l], nums[r]
        elif l_cnt < r_cnt:
            l += 1
            l_cnt += nums[l]
            res += 1
        else:
            r -= 1
            r_cnt += nums[r]
            res += 1
        
    return res
