# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}

        self.prefix = 0

        def tryy(left, right):
            if left > right:
                return None

            root_val = preorder[self.prefix]
            self.prefix += 1

            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            root.left = tryy(left, mid - 1)
            root.right = tryy(mid+1, right)

            return root

        return tryy(0, len(inorder) - 1)
