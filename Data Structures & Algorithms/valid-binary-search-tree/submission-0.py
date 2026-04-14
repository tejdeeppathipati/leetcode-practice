# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isValidNode(root, low, high) ->bool:
            if not root:
                return True

            if low < root.val < high:
                return isValidNode(root.left, low, root.val) and isValidNode(root.right, root.val, high)
            
            return False
         
        return isValidNode(root, float("-inf"), float("inf") )
