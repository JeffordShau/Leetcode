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
        rootIdx = -1
        val = 0
        for num in preorder:
            if num in inorder:
                # print(num)
                rootIdx = inorder.index(num)
                val = num
                break
        # print(\rootIdx\, rootIdx)
        root = TreeNode(num)
        preorder.remove(val)
        root.left = self.buildTree(preorder, inorder[:rootIdx]) if rootIdx != 0 else None
        root.right = self.buildTree(preorder, inorder[rootIdx + 1:]) if rootIdx != len(inorder) else None
        return root
        
        



        
        

