# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # recursively decide the lowest - 
        if (p.val > root.val > q.val) or (p.val < root.val < q.val):
            return root
        
        elif p.val == root.val or q.val == root.val:
            return root

        elif p.val > root.val and  q.val > root.val:
            return self.lowestCommonAncestor(root = root.right, p=p, q=q)
      
        elif p.val < root.val and  q.val < root.val:
            return self.lowestCommonAncestor(root = root.left, p=p, q=q)

        

        


