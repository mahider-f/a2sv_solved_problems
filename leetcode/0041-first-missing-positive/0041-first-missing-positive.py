class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1
        
        for i in range(len(nums)):
            if (nums[i] < 1) or (i >= 1 and nums[i] == nums[i-1]):
                continue
            elif nums[i] == ans:
                ans+=1
            else:
                return ans
        return ans