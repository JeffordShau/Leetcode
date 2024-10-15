# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.order = []
        if not root: 
            return True
        def inorderTraversal(root: Optional[TreeNode]) -> bool:
            if not root:
                return True
            left = inorderTraversal(root.left)
            if not self.order:
                self.order.append(root.val)
            elif self.order[-1] >= root.val:
                return False
            self.order.append(root.val)
            right = inorderTraversal(root.right)
            return left and right
        return inorderTraversal(root)
        