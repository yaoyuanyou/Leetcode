# https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return
        res = ListNode()
        pointer = res
        while head:
            if head.val == val:
                head = head.next
                continue

            pointer.next = head
            head = head.next
            pointer = pointer.next
        pointer.next = head
        return res.next
