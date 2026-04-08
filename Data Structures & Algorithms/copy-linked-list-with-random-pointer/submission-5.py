"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # tp
        hashmap = {None:None}
        tail = head
        while tail:
            newNode = Node(tail.val)
            hashmap[tail] = newNode
            tail = tail.next

        tail = head
        copy = hashmap[head]
        while tail:
            copy.next = hashmap[tail.next]
            copy.random = hashmap[tail.random]
            tail = tail.next
            copy = copy.next

        return hashmap[head]

        



        