# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        parentLevel = []
        childLevel = []
        result = []

        if root:
            parentLevel.append(root)
        while parentLevel:
            level = []
            for parent in parentLevel:
                level.append(parent.val)
                if parent.left:
                    childLevel.append(parent.left)
                if parent.right:
                    childLevel.append(parent.right)
            result.append(level)
            parentLevel = []
            parentLevel, childLevel = childLevel, parentLevel
        return result
                
