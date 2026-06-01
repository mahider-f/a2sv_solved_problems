class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) ->bool:
        if valueDiff < 0:
            return False

        w = valueDiff + 1
        buckets = {}

        for i, num in enumerate(nums):
            b = num // w

            # same bucket
            if b in buckets:
                return True

            # left bucket
            if b - 1 in buckets and abs(num - buckets[b - 1]) <= valueDiff:
                return True

            # right bucket
            if b + 1 in buckets and abs(num - buckets[b + 1]) <= valueDiff:
                return True

            buckets[b] = num

            if i >= indexDiff:
                old = nums[i - indexDiff]
                del buckets[old // w]

        return False