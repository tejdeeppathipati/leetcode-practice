# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution: 
    def check(self,root1, root2):
        if (root1 and not root2) or (not root1 and root2):
            return False
        if not root1 and not root2:
            return True
        
        if root1.val != root2.val:
            return False

        l = self.check(root1.left, root2.left)
        r = self.check(root1.right, root2.right)

        return (l and r)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False
        
        if self.check(root, subRoot):
            return True
        
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)

        return (l or r) 