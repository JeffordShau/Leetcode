# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # print(segment)
        if not inorder or not preorder:
            return None
        rootVal = preorder[0]
        rootIdx = inorder.index(rootVal)
        root = TreeNode(rootVal)
        root.left = self.buildTree(preorder[1:rootIdx + 1], inorder[:rootIdx])
        root.right = self.buildTree(preorder[rootIdx + 1:], inorder[rootIdx + 1:])
        return root
        
        



        
        

