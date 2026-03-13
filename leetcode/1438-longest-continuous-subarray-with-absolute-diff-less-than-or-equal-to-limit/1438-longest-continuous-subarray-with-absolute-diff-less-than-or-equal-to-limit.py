class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_ =deque()
        max_ =deque()

        left, result = 0, 0

        for right in range(len(nums)):
            while min_ and nums[right] < min_[-1]:
                min_.pop()
            min_.append(nums[right])

            while max_ and nums[right] > max_[-1]:
                max_.pop()
            max_.append(nums[right])

            while max_[0] - min_[0] > limit:
                if nums[left] == max_[0]:
                    max_.popleft()
                if nums[left] == min_[0]:
                    min_.popleft()
                left+=1
            result = max(result, right-left+1)
        return result

        