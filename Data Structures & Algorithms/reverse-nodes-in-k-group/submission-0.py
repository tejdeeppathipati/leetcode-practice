# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy_head = ListNode(0, head)
        group_prev = dummy_head

        while True:
            dummy2 = group_prev
            i = 0
            while i < k and dummy2.next:
                dummy2 = dummy2.next
                i += 1
            if i < k:  # fewer than k nodes remain
                break

            # reverse exactly k nodes: [group_prev.next .. dummy2]
            prev = dummy2.next          
            curr = group_prev.next      
            j = 0
            while j < k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                j += 1

            old_head = group_prev.next
            group_prev.next = prev
            group_prev = old_head

        return dummy_head.next