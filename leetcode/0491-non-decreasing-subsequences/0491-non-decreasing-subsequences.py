class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, number):
            if len(number) >= 2:
                ans.append(number[:])
                # return
            
            for i in range(start, len(nums)):
                if number and nums[i] < number[-1]:
                    continue
                number.append(nums[i])
                backtrack(i + 1, number)
                number.pop()
                # print(start, number)
        
        ans = []
        backtrack(0, [])
        stack = []
        for x in ans:
            if x in stack:
                continue
            else:
                stack.append(x)
        return stack
        