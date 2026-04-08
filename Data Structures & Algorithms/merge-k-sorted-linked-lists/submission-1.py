# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        while True:
            minVal = float('inf')
            for i in range(len(lists)):
                if lists[i] != None and lists[i].val < minVal:
                    minVal = lists[i].val
                    num = i 

            if minVal == float('inf'):
                break

            tail.next = lists[num]
            lists[num] = lists[num].next
            tail = tail.next
                
        return dummy.next
        