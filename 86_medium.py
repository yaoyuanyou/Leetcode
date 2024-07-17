# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = less = ListNode(0)
        greater_head = greater = ListNode(0)
        
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        
        greater.next = None  # Important to avoid cyclic links
        less.next = greater_head.next  # Concatenate the two lists
        
        return less_head.next
