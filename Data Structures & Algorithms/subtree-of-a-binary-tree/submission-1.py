# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

#1. find the common point - where the node val main tree = node val subtree
# after - do a recursive dfs - to find if they are the same 

class Solution: 
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True 
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root, subRoot) -> bool:

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        l = self.sameTree(root.left, subRoot.left)
        r = self.sameTree(root.right, subRoot.right)

        if root.val == subRoot.val:
            if l and r:
                return True 
                
        return False






