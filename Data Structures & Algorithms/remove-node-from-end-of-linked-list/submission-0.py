# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l1 = 0
        dummy = head
        while dummy:
            dummy = dummy.next 
            l1 += 1
        
        index = l1 - n
        dummy = head
        prev = None
        l2 = 0

        while dummy:
            if index == l2:
                if l2 == 0:
                    head = head.next
                else:
                    prev.next = dummy.next
                    dummy.next = None 
                return head
            prev = dummy
            dummy = dummy.next
            l2 += 1
        
        return None
            