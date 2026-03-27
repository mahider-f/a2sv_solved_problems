# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0

        def check(node):
            if not node:
                return True,float('inf'),float('-inf'),0

            l,l_min,l_max,l_sum = check(node.left)
            r,r_min,r_max,r_sum = check(node.right)
            
            if l and r and l_max < node.val < r_min:
                cur_sum = node.val + l_sum + r_sum
                self.max_sum = max(self.max_sum,cur_sum)

                return True, min(l_min, r_min, node.val), max(l_max, r_max, node.val), cur_sum

            return False,0,0,0 

        check(root)

        return self.max_sum




            

        