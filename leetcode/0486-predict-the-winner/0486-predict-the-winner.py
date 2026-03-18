class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def winner(i, j):
            if i == j:
                return nums[i]
            left = nums[i] - winner(i+1, j)
            right = nums[j] - winner(i, j-1)

            return max(left, right)
        return winner(0, len(nums)-1) >= 0

