# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None:
            return q is None

        if q is None:
            return p is None

        stack1 = [p]
        stack2 = [q]

        while stack1 and stack2:
            current1 = stack1.pop()
            current2 = stack2.pop()

            if current1 is None and current2 is None:
                continue
            elif current1 is None or current2 is None:
                return False
            elif current1.val != current2.val:
                return False

            stack1.append(current1.left)
            stack2.append(current2.left)

            stack1.append(current1.right)
            stack2.append(current2.right)

        return not stack1 and not stack2