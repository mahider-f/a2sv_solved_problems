class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, number):
            ans.append(sorted(number[:]))
            
            for i in range(start, len(nums)):
                number.append(nums[i])
                backtrack(i + 1, number)
                number.pop()
        
        ans = []
        backtrack(0, [])
        stack = []
        for x in ans:
            if x in stack:
                continue
            else:
                stack.append(x)
        return stack