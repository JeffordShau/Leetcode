# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root: TreeNode, maxVal: int) -> int:
            if not root: 
                return 0
            elif root.val >= maxVal:
                maxVal = root.val
                return 1 + dfs(root.left, maxVal) + dfs(root.right, maxVal)
            return dfs(root.left, maxVal) + dfs(root.right, maxVal)
        return dfs(root, root.val)