class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        heights.append(-1) 
        stack = []
        ans = 0
        for i in range(0, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                currentLowestBarIndex = stack.pop()
                h = heights[currentLowestBarIndex]

                w = i - stack[-1] - 1 if stack else i
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()

        return ans