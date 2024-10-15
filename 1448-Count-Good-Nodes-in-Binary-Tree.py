# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 1

        def dfs(root: TreeNode, maxVal: int) -> None:
            if not root: 
                return
            elif root.val >= maxVal:
                self.counter += 1
            maxVal = max(root.val, maxVal)
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)
        
        dfs(root.left, root.val)
        dfs(root.right, root.val)

        return self.counter