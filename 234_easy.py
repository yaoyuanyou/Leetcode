# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Time Complexity O(n)
#Space Complexity O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        
        l, r = 0, len(lst) - 1
        while l < r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1
        return True

#Time Complexity O(n)
#Space Complexity O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next =prev
            prev = slow
            slow = nxt
        
        if not fast:
            LL_L, LL_R = prev, slow
        else:
            LL_L, LL_R = prev, slow.next

        while LL_L:
            if LL_L.val != LL_R.val:
                return False
            LL_L = LL_L.next
            LL_R = LL_R.next
        
        return True
