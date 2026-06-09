class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        st = set(nums)
        numss = list(st)
        numss.sort()
        if len(numss) >= 3:
            return numss[-3]
        return max(nums)
