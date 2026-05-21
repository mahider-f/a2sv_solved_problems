class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        if len(nums) == 1:
            return nums[0]

        def dfs(i,flag):
            if i>= len(nums):
                return 0
            
            if (i,flag) in dp:
                return dp[(i, flag)]

            if i == len(nums) - 1 and flag:
                return 0
            skip = dfs(i+1,flag)
            rob = dfs(i+2, flag or (i == 0)) + nums[i]

            dp[(i,flag)] = max(rob,skip)
            return dp[(i,flag)]

        a = dfs(0,True)
        b = dfs(1, False)

        return max(a,b)

