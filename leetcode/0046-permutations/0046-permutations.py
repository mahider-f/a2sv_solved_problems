class Solution:
    def permute(self, nums):
        res = []

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = 1
                    path.append(nums[i])
                    backtrack(path, used)
                    path.pop()
                    used[i] = 0

        backtrack([], [0] * len(nums))
        return res
