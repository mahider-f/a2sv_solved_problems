class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort(reverse = True)
        # stack = []
        # stack.append(intervals[0])
        # count = 0
        # i = 1

        # while stack and i < len(intervals):
        #     if stack[-1][0] >= intervals[i][0] and stack[-1][1] <= intervals[i][1]:
        #         stack.pop()
        #     stack.append(intervals[i])
        #     i+=1


        # return len(stack)
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        max_end = 0

        for start, end in intervals:
            if end <= max_end:
                count += 1
            else:
                max_end = end

        return len(intervals) - count