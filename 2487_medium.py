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


#Space Complexity O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        maximum = prev.val

        curr = prev
         
        while curr.next:
            if curr.next.val >= curr.val:
                maximum = curr.next.val
                curr = curr.next
            else:
                curr.next = curr.next.next
        curr.next = None
        
        curr = prev
        reverse = None
        while curr:
            temp = curr.next
            curr.next = reverse
            reverse = curr
            curr = temp

        return reverse
