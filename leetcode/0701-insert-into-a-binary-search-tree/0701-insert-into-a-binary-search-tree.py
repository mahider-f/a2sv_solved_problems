# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> Optional[TreeNode]:

        def answer(root):
            if not root:
                return TreeNode(val)
            if root.val < val:
                root.right = answer(root.right)
            else:
                root.left = answer(root.left)
            return root

        return answer(root)
        
