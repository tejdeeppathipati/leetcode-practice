# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def theDepth(self, root):
        if not root: 
            return 0 
        l = 1 + self.theDepth(root.left)
        r = 1 + self.theDepth(root.right)
        return max(l,r)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        maxD = 0 
        while stack:
            node = stack.pop()
            currD = self.theDepth(node.right) + self.theDepth(node.left)
            maxD = max(maxD, currD)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return maxD