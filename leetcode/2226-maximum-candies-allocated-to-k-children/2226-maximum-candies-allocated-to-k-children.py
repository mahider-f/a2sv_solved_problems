class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(num):
            count = 0

            for candy in candies:
                count += candy//num
            return count >= k

        l, r = 1, max(candies)
        while l <= r:
            mid = (l+r) // 2

            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r