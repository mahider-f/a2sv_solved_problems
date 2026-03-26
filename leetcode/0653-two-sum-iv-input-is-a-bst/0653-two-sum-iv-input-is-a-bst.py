# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        ans = []

        def answer(node):
            if not node:
                return 
            answer(node.left)
            ans.append(node.val)
            answer(node.right)

        answer(root)
        print(ans)
        Ans = Counter(ans)
        if len(ans) <2:
            return False

        for x in Ans:
            diff = k - x
            if diff == x and Ans[x] >1:
                return True
            if diff != x and diff in Ans:
                return True
        return False