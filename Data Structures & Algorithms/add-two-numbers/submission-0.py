# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1, t2 = l1, l2
        dummy = ListNode()
        tail = dummy
        carry = 0
        while t1 or t2:
            val1, val2 = 0,0
            if t1:
                val1 = t1.val 
                t1 = t1.next
            if t2:
                val2 = t2.val
                t2 = t2.next

            val = val1 + val2 + carry 
            if val >= 10:
                carry = 1
                val = val - 10
            else:
                carry = 0 
            tail.next = ListNode(val)
            tail = tail.next

        if carry == 1:
            tail.next = ListNode(carry)
        
        return dummy.next





            
                