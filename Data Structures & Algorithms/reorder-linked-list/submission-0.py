# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        newhead = slow.next
        prev = None 
        while newhead:
            temp = newhead.next
            newhead.next = prev
            prev = newhead
            newhead = temp

        slow.next = None
        tail = head
        while tail and tail.next:
            temp1, temp2 = tail.next, prev.next
            tail.next = prev
            prev.next = temp1
            prev = temp2
            tail = tail.next.next

        tail.next = prev




        
        
