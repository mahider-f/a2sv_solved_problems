class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        
        nums.sort()
        
        m = 0
        for i in range(1, len(nums)):
            m = max(m, nums[i] - nums[i-1])
        
        return m