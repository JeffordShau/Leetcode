# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        result = []
        if not root:
            return []
        q.append(root)
        while True:
            children = []
            currLevel = []
            while q:
                curr = q.popleft()
                currLevel.append(curr.val)
                if curr.left:
                    children.append(curr.left)
                if curr.right:
                    children.append(curr.right)
            result.append(currLevel)
            if children:
                q = deque(children)
            else:
                break
        return result
            