class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, number):
            ans.append(number[:])
            
            for i in range(start, len(nums)):
                number.append(nums[i])
                backtrack(i + 1, number)
                number.pop()
        
        ans = []
        backtrack(0, [])
        return ans