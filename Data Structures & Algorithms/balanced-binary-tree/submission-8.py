# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, node):
        if not node:
            return 0
        l = 1 + self.check(node.left)
        r = 1 + self.check(node.right)

        return max(l,r)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:  
        if not root:
            return True
        left = self.check(root.left)
        right = self.check(root.right)

        if abs(left - right) > 1:
            return False

        return (self.isBalanced(root.left) and self.isBalanced(root.right))
        
