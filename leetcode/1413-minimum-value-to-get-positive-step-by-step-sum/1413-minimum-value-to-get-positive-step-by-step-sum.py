class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        res = [0]*(len(nums)+1)

        for i in range(1,len(nums)+1):
            res[i] = res[i-1] + nums[i-1]
        res.pop(0)
        a = min(res)
        return ((abs(a)+1) if a < 0 else 1)
        

        