# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        curr = head
        index = 1
        prev = None

        while index <= right:
            if index < left:
                prev = curr
                curr = curr.next
            elif index == left:
                left_node = prev
                left_reverse_node = curr
                temp = curr.next
                curr.next = prev
                prev = curr                
                curr = temp
                
                
            else:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                print(prev)
            index += 1

        left_reverse_node.next = curr   
        if left != 1:
            left_node.next = prev
        else:
            return prev
        
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        for _ in range(1, left):
            curr = curr.next
        
        first_left  = curr
        curr = curr.next
        second_right = curr
        prev = None
        
        for _ in range(left, right + 1):
            temp = curr
            curr.next, curr = prev, curr.next
            prev = temp


        first_left.next = prev
        second_right.next = curr
        return dummy.next
