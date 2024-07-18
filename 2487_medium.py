# Time Complexity O(n)
# Space Complexity O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        compare = self.removeNodes(head.next)
        if head.val >= compare.val:
            head.next = compare
            return head
        else:
            return compare
