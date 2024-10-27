# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = collections.deque(preorder)

        hashMap = {}
        for idx, num in enumerate(inorder):
            hashMap[num] = idx

        def helper(start: int, end: int):
            if start > end:
                return None
            root = TreeNode(preorder.popleft())
            mid = hashMap[root.val]
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root
            
        return helper(0, len(preorder) - 1)
        
        



        
        

