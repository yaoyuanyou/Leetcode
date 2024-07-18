# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        last = None
        cnt = 0

        while curr:
            cnt += 1
            last = curr
            curr = curr.next
        
        k = k % cnt
        if k == 0 :
            return head

        curr = head

        for _ in range(1, cnt - k):
            curr = curr.next
        
        curr.next, new_head = None, curr.next
        last.next = head
        
        return new_head
