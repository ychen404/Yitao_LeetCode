# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r: TreeNode):
            if r: 
                return inorder(r.left) + [r.val] + inorder(r.right)
            else:
                return []
        
        return min(inorder(root), key = lambda x: abs(target - x))
            
