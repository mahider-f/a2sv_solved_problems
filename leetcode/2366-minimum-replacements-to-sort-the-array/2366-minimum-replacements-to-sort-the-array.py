class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        prev = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= prev:
                prev = nums[i]
            else:
                k = (nums[i] + prev - 1) // prev  
                count += k - 1
                prev = nums[i] // k

        return count