# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        max_ = max(nums)
        root = TreeNode(max_)
        x = nums.index(max_)
        root.left = self.constructMaximumBinaryTree(nums[:x])
        root.right = self.constructMaximumBinaryTree(nums[x+1:])

        return root