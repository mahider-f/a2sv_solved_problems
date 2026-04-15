class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i+1 not in nums:
                b = i+1
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        a = [v for i, v in enumerate(nums) if v != i + 1]
        a.append(b) 
        return a
