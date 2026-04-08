# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        count = 0
        prev = None
        while fast:
            fast = fast.next
            if count >= n :
                prev = slow
                slow = slow.next
            count += 1
        
        if not prev:
            head = head.next
        else:
            prev.next = slow.next
        return head
