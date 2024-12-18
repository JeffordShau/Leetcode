# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode], left: int, right: int) -> bool:
            if not root:
                return True
            elif root.val < right and root.val > left:
                return helper(root.left, left, root.val) and helper(root.right, root.val, right)
            else:
                return False
        return helper(root, float('-inf'), float('inf'))