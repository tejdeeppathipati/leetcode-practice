# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1, t2 = l1, l2
        # prev = ListNode()
        carry = 0 
        while t1 or t2 or carry:
            val1 = t1.val if t1 else 0
            val2 = t2.val if t2 else 0
            total = val1 + val2 + carry 

            if  total >= 10:
                carry = 1
                val = total - 10
            else:
                carry = 0 
                val = total

            if not t2:
                t2 = ListNode()
                prev.next = t2
    
            t2.val = val
            prev = t2
            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next
    
        return l2
                