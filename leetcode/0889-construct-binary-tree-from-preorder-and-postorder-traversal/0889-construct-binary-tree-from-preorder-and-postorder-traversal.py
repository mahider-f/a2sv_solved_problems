# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
        
        left_root = preorder[1]
        i = postorder.index(left_root)
        
        root.left = self.constructFromPrePost(preorder[1:i+2],postorder[:i+1])
        
        root.right = self.constructFromPrePost(preorder[i+2:],postorder[i+1:-1])
        
        return root