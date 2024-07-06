#Initial 55mins
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1, curr_2 = l1, l2
        plus = (curr_1.val + curr_2.val) // 10

        ans = ListNode((curr_1.val + curr_2.val) % 10)
        ind = ans

        curr_1, curr_2 = curr_1.next, curr_2.next

        while curr_1 and curr_2:
            
            ind.next = ListNode()
            ind = ind.next

            if curr_1.val + curr_2.val + plus >= 10:
                ind.val = curr_1.val + curr_2.val + plus - 10
                plus = 1
            else:
                ind.val = curr_1.val + curr_2.val + plus
                plus = 0
            
            curr_1 = curr_1.next
            curr_2 = curr_2.next
            
        if curr_1:
            while curr_1:

                ind.next = ListNode()
                ind = ind.next

                if curr_1.val + plus >= 10:
                    ind.val = curr_1.val + plus - 10
                    plus = 1
                else:
                    ind.val = curr_1.val + plus
                    plus = 0
                curr_1 = curr_1.next
                
                
        else:
            while curr_2:
                ind.next = ListNode()
                ind = ind.next
                
                if curr_2.val + plus >= 10:
                    ind.val = curr_2.val + plus - 10
                    plus = 1
                else:
                    ind.val = curr_2.val + plus
                    plus = 0
                curr_2 = curr_2.next


        if plus == 1:
            ind.next = ListNode(1)

        
        return ans 


#More Concise
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        curr = ans
        carry = 0

        while l1 or l2 or carry:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            val = first + second + carry
            curr.next = ListNode(val % 10)
            curr = curr.next
            carry = val // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return ans.next
