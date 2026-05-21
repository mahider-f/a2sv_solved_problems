class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(i,total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0

            if (i,total) in dp:
                return dp[(i,total)]

            add = total + nums[i]
            subtract = total - nums[i]
            dp[(i,total)] = (backtrack(i+1,add) + backtrack(i+1,subtract))
            return dp[(i,total)]
        return backtrack(0,0)